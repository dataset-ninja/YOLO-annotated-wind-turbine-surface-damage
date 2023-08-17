Dataset **YOLO Annotated Wind Turbine Surface Damage** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/f/8/g3/SEaE1EacQQqm0Wu0aBB2l1Z1WC3ZZUBLllBgGkFwwJ4qUut9arhTrWZ1dLZ16w1f9NK8opXflCLt61qbbdq0T2szVtPIRVxoz6cUa9WnGZb2AIUiGpNT37DSCGbZ.tar)

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