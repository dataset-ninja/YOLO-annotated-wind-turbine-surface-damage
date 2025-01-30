Dataset **YOLO Annotated Wind Turbine Surface Damage** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzExMTBfWU9MTyBBbm5vdGF0ZWQgV2luZCBUdXJiaW5lIFN1cmZhY2UgRGFtYWdlL3lvbG8tYW5ub3RhdGVkLXdpbmQtdHVyYmluZS1zdXJmYWNlLWRhbWFnZS1EYXRhc2V0TmluamEudGFyIiwgInNpZyI6ICJXYS9ZYW1pNjdkVWJjdm8rQ3pHeE5IL3I1dzVmeTJHRXhoK1NJODVmZEQ0PSJ9)

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