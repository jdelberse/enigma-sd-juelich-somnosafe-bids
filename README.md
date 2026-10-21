# Cologne "Somnosafe" Dataset (`juelich-somnosafe-bids`)

## Overview
**NB**: This dataset was shared and maintained under the name `juelich-somnosafe-bids`, which could not be changed. This dataset is one of two datasets (`juelich-petcoffee-bids` and `juelich-somnosafe-bids`) that make up the Cologne sample.

This dataset contains MRI data from a sleep manipulation study conducted at the German Aerospace Center (Germany). It is part of the ENIGMA-Sleep Working Group collection used to study the effects of sleep loss on glymphatic MRI indices. The data are organized according to the Brain Imaging Data Structure (BIDS) and managed with DataLad (git-annex).

## Sample

| Item | Value |
|---|---|
| Site | Cologne |
| Affiliation | German Aerospace Center |
| Country | Germany |
| Participants (N) | 48 |
| Age, mean (SD), years | 27.5 (4.9) |
| Male (%) | 60.4 |

## Sleep protocol

- **BL**: baseline, habitual sleep
- **SD**: total sleep deprivation, 24h
- **SR**: sleep restriction, 5h TIB

## Imaging data

### T1-weighted (`anat/`)

| Parameter | Value |
|---|---|
| Scanner | Siemens Biograph mMR |
| Sequence | MPRAGE |
| TR (ms) | 2250 |
| TE (ms) | 3.03 |
| TI (ms) | 900 |
| Flip angle (°) | 9 |

## Data organization

- `sub-<ID>/ses-<label>/`: raw BIDS data (`anat/`)
- `participants.tsv`: participant-level information
- `sub-<ID>/sub-<ID>_sessions.tsv`: session-level information (condition, visit, date, time)
- `derivatives/`: processed outputs, if present

File contents are tracked with git-annex. After cloning, retrieve data with `datalad get <path>`.

## Original publication

Hennecke, E., Lange, D., Steenbergen, F., Fronczek-Poncelet, J., Elmenhorst, D., Bauer, A., Aeschbach, D., & Elmenhorst, E.-M. (2021). Adverse interaction effects of chronic and acute sleep deficits on spatial working memory but not on verbal working memory or declarative memory. *Journal of Sleep Research*, 30(4), e13225. [https://doi.org/10.1111/jsr.13225](https://doi.org/10.1111/jsr.13225)

## Contact

- Jorik D. Elberse: [j.elberse@fz-juelich.de](mailto:j.elberse@fz-juelich.de)
- Masoud Tahmasian: [m.tahmasian@fz-juelich.de](mailto:m.tahmasian@fz-juelich.de)