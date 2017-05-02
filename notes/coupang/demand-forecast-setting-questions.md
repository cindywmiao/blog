demand-forecast-setting-questions.md

BUILD your local PYTHON environment 
=== 
# download anaconda2 from www.continuum.io/downloads 
bash Anaconda*.sh
# create env with python3.x and science modules 
conda create --name py3x python=3 scikit-learn==0.17.1 scipy==0.17.1 requests pandas==0.18.1 numpy==1.11.1 statsmodels==0.6.1
# activate environnement 
source activate py3x
USE pyinstaller to make the executable file which could be executed on Clouldera(NCDS) 
=== 
# install pyinstaller with no conflict version 
conda install -c conda-forge pyinstaller=3.2
# downgrade setuptools due to dependency conflicts 
conda install setuptools==19.2
# fix issue: Intel MKL FATAL ERROR: Cannot load libmkl_avx.so or libmkl_def.so · Issue #3884 · BVLC/caffe 
conda install nomkl
# check packages 
conda list
# build the executable file. 
1. go the bin folder 
2. execute: 
pyinstaller --hidden-import sklearn.neighbors.typedefs -F forecast_executor.py
===
# disactivate environnement 
source disactivate environnement


# note by cindy
conda install -c anaconda configparser=3.5.0
=> install pyparsing