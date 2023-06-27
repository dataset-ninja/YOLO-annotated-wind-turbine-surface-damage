Dataset **Wind Turbines 7** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/0/M/Ob/az6n2g8e0aOfR3Q2HFplGc31VbtYScWIj9TSvEcE01GoAVTPivyWnmcqO2C0oVNZwyu5nFRcWxiBgVghBNuTGQYyA6SvIn8Tfx0KqKTQhkokjgqOSfNuijLkWiMl.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Wind Turbines 7', dst_path='~/dtools/datasets/Wind Turbines 7.tar')
```
The data in original format can be 🔗[downloaded here](https://www.kaggle.com/datasets/ajifoster3/yolo-annotated-wind-turbines-586x371/download?datasetVersionNumber=1)