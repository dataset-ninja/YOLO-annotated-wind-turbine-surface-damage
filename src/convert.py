# Path to the original dataset

import os

import gdown
import supervisely as sly
from dataset_tools.convert import unpack_if_archive
from tqdm import tqdm

import src.settings as s


def download_dataset():
    archive_path = os.path.join(sly.app.get_data_dir(), "archive.zip")

    if not os.path.exists(archive_path):
        if isinstance(s.DOWNLOAD_ORIGINAL_URL, str):
            gdown.download(s.DOWNLOAD_ORIGINAL_URL, archive_path, quiet=False)
        if isinstance(s.DOWNLOAD_ORIGINAL_URL, dict):
            for name, url in s.DOWNLOAD_ORIGINAL_URL:
                gdown.download(url, os.path.join(archive_path, name), quiet=False)
    else:
        sly.logger.info(f"Path '{archive_path}' already exists.")
    return unpack_if_archive(archive_path)


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    images_dirname = "images"
    anns_dirname = "labels"
    batch_size = 30

    def _create_ann(ann_path, image_path):
        labels = []

        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        img_height = image_np.shape[0]
        img_wight = image_np.shape[1]
        if sly.fs.file_exists(ann_path):
            with open(ann_path) as f:
                content = f.read().split("\n")
                for line in content:
                    if content == ["dirt", "damage"]:
                        continue
                    if len(line) != 0:
                        line = list(map(float, line.split(" ")))
                        obj_class = idx_to_class[int(line[0])]

                        left = int((line[1] - line[3] / 2) * img_wight)
                        right = int((line[1] + line[3] / 2) * img_wight)
                        top = int((line[2] - line[4] / 2) * img_height)
                        bottom = int((line[2] + line[4] / 2) * img_height)
                        rectangle = sly.Rectangle(top=top, left=left, bottom=bottom, right=right)
                        label = sly.Label(rectangle, obj_class)
                        labels.append(label)

        return sly.Annotation(img_size=(img_height, img_wight), labels=labels)

    remote_path = "/4import/YOLO Annotated Wind Turbine Surface Damage/archive.zip"
    local_path = os.path.join(sly.app.get_data_dir(), "archive.zip")
    file_info = api.file.get_info_by_path(sly.env.team_id(), remote_path)
    download_progress = tqdm(desc="Download dataset", total=file_info.sizeb)
    api.file.download(
        sly.env.team_id(), remote_path, local_path, progress_cb=download_progress.update
    )

    local_path = unpack_if_archive(local_path)
    local_path = os.path.join(local_path, "NordTank586x371")
    project = api.project.create(workspace_id, project_name)
    dirt_obj_class = sly.ObjClass("dirt", sly.Rectangle)
    damage_obj_class = sly.ObjClass("damage", sly.Rectangle)
    meta = sly.ProjectMeta(obj_classes=[dirt_obj_class, damage_obj_class])
    api.project.update_meta(project.id, meta.to_json())

    dataset_train = api.dataset.create(project.id, "train")

    images_dir = os.path.join(local_path, images_dirname)
    anns_dir = os.path.join(local_path, anns_dirname)

    images_names = os.listdir(images_dir)

    idx_to_class = {0: dirt_obj_class, 1: damage_obj_class}

    progress = tqdm(desc=f'Create dataset "train"', total=len(images_names))
    for imgs_batch in sly.batched(images_names, batch_size=batch_size):
        images_pathes = [os.path.join(images_dir, name) for name in imgs_batch]

        anns_names = [f"{sly.fs.get_file_name(name)}.txt" for name in imgs_batch]
        anns_pathes = [os.path.join(anns_dir, name) for name in anns_names]

        img_infos = api.image.upload_paths(dataset_train.id, imgs_batch, images_pathes)
        img_ids = [im_info.id for im_info in img_infos]

        anns_batch = [_create_ann(*paths) for paths in zip(anns_pathes, images_pathes)]
        api.annotation.upload_anns(img_ids, anns_batch)

        progress.update(len(imgs_batch))

    return project
