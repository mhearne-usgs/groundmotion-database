Status
=======
[![Build Status](https://travis-ci.org/usgs/strongmotion-database.svg?branch=master)](https://travis-ci.org/usgs/strongmotion-database)

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/552718dc32df4218b2037084f9143702)](https://www.codacy.com/app/hschovanec-usgs/strongmotion-database?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=usgs/strongmotion-database&amp;utm_campaign=Badge_Grade)

[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/552718dc32df4218b2037084f9143702)](https://www.codacy.com/app/hschovanec-usgs/strongmotion-database?utm_source=github.com&utm_medium=referral&utm_content=usgs/strongmotion-database&utm_campaign=Badge_Coverage)


strongmotion-database
=====

Fetch and process strong motion waveform/peak amplitude data.

# Introduction

strongmotion-database is a project designed to facilitate the loading of
strong motion time series data and parametric data into databases.
This repository includes the following tools:

 * `getpgm` : gathers pgm values from a directory of strong motion files and
and outputs simple flatfiles and tables of IMC and IMT values.

# Installing

If you already have a miniconda or anaconda Python 3.X environment:

 - `conda install numpy`
 - `conda install pandas`
 - `conda install openpyxl`
 - `conda install lxml`
 - `pip install git+https://github.com/usgs/strongmotion-database.git`

If you do not have anaconda or miniconda, but have Python 3.X installed with pip:
 - `pip install numpy`
 - `pip install pandas`
 - `pip install openpyxl`
 - `pip install lxml`
 - `pip install git+https://github.com/usgs/strongmotion-database.git`

## Updating

 - `pip install --upgrade git+https://github.com/usgs/strongmotion-database.git`

# Tools

## getpgm

This tool presumes there is a directory containing files of strong ground
motion data as time series, in a format supported by amptools. At this time
time series must be acceleration.

Supported formats include:
- [COSMOS](https://strongmotioncenter.org/vdc/cosmos_format_1_20.pdf
)
- CWB
- [DMG](ftp://ftp.consrv.ca.gov/pub/dmg/csmip/Formats/DMGformat85.pdf
) (synonymous to CSMIP)
- [GEONET](https://www.geonet.org.nz/data/supplementary/strong_motion_file_formats)
- [KNET](http://www.kyoshin.bosai.go.jp/kyoshin/man/knetform_en.html
)
- [SMC](https://escweb.wr.usgs.gov/nsmp-data/smcfmt.html
)
- [USC](https://strongmotioncenter.org/vdc/USC_Vol1Format.txt)

### Use
getpgm [-h] -c COMPONENTS [COMPONENTS ...] -m MEASUREMENTS
              [MEASUREMENTS ...] [-t] [-p]
              input_source output_directory

Get requested PGM values.


#### Positional arguments

  input_source:          The directory of all input files.

  output_directory:      The directory of all output files.

#### Optional arguments

  -h, --help:            show this help message and exit

  -c COMPONENTS [COMPONENTS ...], --components COMPONENTS [COMPONENTS ...]:
                        The IMC parameters to get.


  -m MEASUREMENTS [MEASUREMENTS ...], --measurements MEASUREMENTS [MEASUREMENTS ...]:
                        The IMT parameters to get.


  -t, --timeseries:      Writes out the uncorrected time series for each
                        station in miniseed.


  -p, --parametric:      Writes out the parametric data for each station.

#### PGM Parameters
Available IMTs:
- pga
- sa
- pgv

Available IMCs:
- greater_of_two_horizontals
- channels
- gmrotd

#### For parameters with specific percentiles or periods, append the number on the end of the parameter string.

Example spectral amplitude: sa1.0

Example geometric mean rotation: gmrotd50
