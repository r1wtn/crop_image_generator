# CROP IMAGE GENERATOR 

## Install

on Python 3.9.2

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Poisson Image Editing
Cloned from 
[https://github.com/rinsa318/poisson-image-editing](https://github.com/rinsa318/poisson-image-editing)


```bash
cd tests/
python test_make_mask.py    # to make src and mask image
python test_poisson_blend.py    # take 200 ~ seconds
```