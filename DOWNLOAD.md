Dataset **Wind Turbine Surface Damage** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/R/0/Sg/Unq90vDx6XkRbcgRkSu9RLvFDYdwl3czAYAUPszlTKpIsiJEPqtH5jqtRJS9syY0klyzyhtzfiNDDZINYO8mPuw72TS7CIfdAAy8aya6CAUve0yTOlTmHmyjbBSd.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Wind Turbine Surface Damage', dst_path='~/dtools/datasets/Wind Turbine Surface Damage.tar')
```
The data in original format can be 🔗[downloaded here](https://www.kaggle.com/datasets/ajifoster3/yolo-annotated-wind-turbines-586x371/download?datasetVersionNumber=1)