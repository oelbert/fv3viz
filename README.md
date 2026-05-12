# FV3Viz
Once upon a time the Allen Institute Climate Modeling (nee Vulcan Climate Modeling) team developed a suite of tools to visualize data from FV3-based atmospheric models by gathering data from cubed-sphere tiles and plotting them. That code is now archived in https://github.com/ai2cm/fv3net but is no longer maintained. This repo tries to keep a working version as dependencies like numpy change.

The original readme follows:

fv3viz
======

This package contains visualization tools used by the Allen Institute for AI Climate Modeling ML team. The package includes three types of functions:
    1. those associated with plotting cubed-sphere tile data as maps using cartopy
    2. common diagnostic plots, and
    3. histograms of set of timesteps useful for describing ML datasets

To get started, see example images and cubed-sphere plotting routines provided in the image gallery.

Note: The default behavior of fv3viz is to redirect external downloads of shapefiles to an internally hosted repo which contains only the global-scale coastlines file. If other files are desired, please set the following environment variable prior to importing fv3viz to use cartopy's source:

```bash
$ export CARTOPY_EXTERNAL_DOWNLOADER="natural_earth"
```
