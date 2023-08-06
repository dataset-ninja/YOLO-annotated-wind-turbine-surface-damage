Dataset **YOLO Annotated Wind Turbine Surface Damage** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/G/I/7Z/wtfpMkNpS5njwQasacfVhsAc9Nq28m26cficbfW1Z4hf6JPMxbQIqRx3INW4fO1DNYt83cDHng98En16dSVeTcezGcR89Gga5fjrTV6aD8Eqq0Y7m0wydRU5LJtF.tar)

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

The data in original format can be [downloaded here](https://www.kaggle.com/datasets/ajifoster3/yolo-annotated-wind-turbines-586x371/download?datasetVersionNumber=1)