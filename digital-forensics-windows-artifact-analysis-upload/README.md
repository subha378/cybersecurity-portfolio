# Digital Forensics Case Study — Windows Artifact Analysis

## Overview
This project is a portfolio-safe version of a simulated digital forensics case study completed using **Autopsy**. The project focused on analysing Windows artifacts, documenting evidence locations, and explaining findings in a structured forensic report.

This public version includes only cleaned documentation and redacted screenshots. It does **not** include the original evidence image, university assessment files, private data, screenshots with readable personal information, or restricted material.

## Evidence Areas Demonstrated
- Evidence source and acquisition review
- OS account artifact analysis
- Communication/application artifact review
- USB device artifact analysis
- Web history analysis
- Installed programs review
- Video file type analysis
- PII and ethical handling considerations

## Tools Used
- Autopsy
- Windows artifact analysis concepts
- Technical reporting and documentation

## Methodology
1. **Chain of custody and integrity review** — Reviewed evidence source details and considered how hashing, evidence logging, and custody records support evidence integrity.
2. **User account analysis** — Used Autopsy's OS account artifacts to review account properties, login activity, privilege level, and password policy indicators.
3. **Communication application review** — Reviewed filesystem and application artifact locations to identify communication-related application traces.
4. **USB/device history analysis** — Reviewed USB device artifacts to understand physical devices connected to the system.
5. **Web activity reconstruction** — Reviewed web history artifacts to identify activity patterns within a defined timeframe.
6. **Software installation timeline** — Reviewed installed program artifacts to build a timeline of software installed within a target window.
7. **Unique media identification** — Reviewed video file artifacts and file paths to distinguish user-generated media from system, application, or cache files.
8. **PII handling** — Identified categories of personally identifiable information and applied ethical handling principles to avoid unnecessary exposure.

## Key Findings Summary
- Identified a primary non-system user account and reviewed its account properties.
- Found traces of communication application usage through filesystem artifacts.
- Identified physical device connection evidence through USB artifacts.
- Reviewed web history to support timeline reconstruction.
- Analysed installed program artifacts to identify software installed during a target period.
- Distinguished potentially user-generated video content from system/application/cache media files.
- Considered privacy and ethics when encountering personally identifiable information.

## Screenshots
The screenshots in the `screenshots/` folder are redacted proof-of-work images. They show tool workflow and analysis areas while removing sensitive case details, personal identifiers, search terms, device IDs, file paths, and assignment-specific data.

## Screenshots Included
1. `01-autopsy-data-source-properties-redacted.png` — Data source/properties review
2. `02-os-account-artifacts-redacted.png` — OS account artifact analysis
3. `03-communication-appdata-artifacts-redacted.png` — Communication/application artifacts
4. `04-usb-device-artifacts-redacted.png` — USB device artifacts
5. `05-web-history-analysis-redacted.png` — Web history analysis
6. `06-installed-programs-artifacts-redacted.png` — Installed programs artifacts
7. `07-video-file-types-redacted.png` — Video file type analysis

## Ethical Considerations
This project applied privacy-aware investigation principles. Unrelated personally identifiable information should be documented only at a category level, minimised, segregated, and not copied or analysed beyond what is necessary for the investigation.

## Skills Demonstrated
- Digital forensic investigation
- Windows artifact analysis
- Chain of custody and evidence integrity assessment
- Registry artifact analysis
- USB history review
- Installed program timeline analysis
- Web history and search activity reconstruction
- File system and metadata analysis
- PII identification and ethical handling
- Technical investigation reporting

## What I Learned
This project strengthened my understanding of how forensic investigators move from raw disk artifacts to a defensible, well-documented narrative. It also improved my ability to use Autopsy, interpret Windows artifacts, document technical findings clearly, and apply privacy and ethical obligations during an investigation.

## Important Note
This repository is for portfolio demonstration only. It does not publish the original assignment, evidence image, raw screenshots with readable PII, private identifiers, device serial numbers, source files, or university-restricted material. Identifying details have been generalised, redacted, or omitted.
