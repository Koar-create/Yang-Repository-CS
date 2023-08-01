import platform
if platform.system() == 'Linux':
    !pip install boto3==1.26.76 --quiet
    !pip install botocore==1.29.76 --quiet
    !pip install pooch==1.7.0 --quiet
    !pip install s3fs==2023.6.0 --quiet
    !pip install cdsapi --quiet
    !pip install --upgrade pandas --quiet
    !pip install xarray --quiet
    !pip install nc_time_axis --quiet
    !pip install cartopy --quiet

    !pip install imageio --quiet
    !pip install imageio[ffmpeg] --quiet
    !pip install imageio[pyav] --quiet

# 1. downloaad
import cdsapi                         # download from Climate Data Store, ECMWF
import pooch, urllib.request          # download from any available URL
import s3fs, boto3, botocore          # download from S3 server, Amazon Web Service

# 2. useful toolkits
from itertools import product
import os, sys, glob, time, tempfile

# 3. read and write
import h5py

# 4. data processing
from scipy import stats
from datetime import datetime, timedelta
import numpy as np, pandas as pd, xarray as xr

# 5. image processing
import imageio
from wordcloud import WordCloud
import cartopy.io.shapereader as shapereader
import matplotlib as mpl, matplotlib.pyplot as plt
import cartopy, cartopy.crs as ccrs, cartopy.feature as cfeature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter
