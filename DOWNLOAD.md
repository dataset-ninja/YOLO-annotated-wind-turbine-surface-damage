Dataset **Wind Turbine 7** can be downloaded in Supervisely format:

 [Download](https://assets.supervise.ly/supervisely-supervisely-assets-public/teams_storage/1/V/c6/PolXznewivXoVZQoPMmNREvsxz1VejeIfy32PlUZv4k45Det9r2JtxcufnP8LbK3F0lXZ3cqiN8iP7xIiNiVSLBH1oRafEAdkQZrZvi8ewaODtFMaSED9H1YWTDv.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Wind Turbine 7', dst_path='~/dtools/datasets/Wind Turbine 7.tar')
```
The data in original format can be 🔗[downloaded here](https://www.kaggle.com/datasets/ajifoster3/yolo-annotated-wind-turbines-586x371/download?datasetVersionNumber=1)