Dataset **YOLO Annotated Wind Turbine Surface Damage** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/3/Z/J1/Ug2ZpHwWEKUs0AVIGlrzB02SlOFPqZG76z6da8C3DM2xoA008PItiazXw0JFMBw4TLviCZKxQ9gzWxjjAQQINztFrm4NLSGWBSpZJGImTH6WTNlDhGjaR5J11Ftj.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='YOLO Annotated Wind Turbine Surface Damage', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://www.kaggle.com/datasets/ajifoster3/yolo-annotated-wind-turbines-586x371/download?datasetVersionNumber=1).