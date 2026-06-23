# Digital Forensics Investigation — Seized Laptop Case Study

## Overview
This project involved conducting a full digital forensic investigation of a seized Windows laptop disk image using **Autopsy**. The goal was to recover and interpret artifacts relevant to a suspected security incident, document the process and findings clearly, and apply ethical and legal considerations when handling digital evidence — particularly around Personally Identifiable Information (PII) encountered along the way.

## Objectives
- Understand and apply chain-of-custody principles in a forensics scenario
- Assess evidence integrity and identify gaps that could be challenged (e.g. missing hash verification)
- Identify and profile active user accounts, login activity, and privilege levels
- Discover third-party communication applications via filesystem and AppData artifacts
- Analyse connected USB/physical device history via registry artifacts
- Reconstruct web search activity within a defined timeframe
- Build an installed-software timeline within a defined timeframe
- Identify unique, user-generated media files versus system/cache files
- Apply the ACS Code of Ethics to the handling of unrelated PII discovered during analysis

## Tools Used
- **Autopsy** — disk image analysis, OS Accounts viewer, Data Artifacts modules, File Types viewer, Web History/Web Search modules

## Methodology
1. **Chain of custody & integrity** — Reviewed the properties of the disk image to check for cryptographic hash metadata; identified that the absence of a recorded hash at acquisition time is itself a vector an opposing party could use to challenge evidence integrity. Documented the three core techniques (hashing, evidence bagging/tagging, custody-form logging) used to establish chain of custody more broadly.
2. **User account analysis** — Used the OS Accounts viewer to enumerate non-system accounts, then drilled into account properties for login count, creation date, privilege flag, and password policy settings.
3. **Communication app discovery** — Cross-referenced the account with the highest login count, then navigated its `AppData\Roaming` directory to identify installed communication clients by folder presence and modification timestamps (used to infer install date and last-active date).
4. **USB/device history** — Used the **USB Device Attached** registry artifact viewer to pull connection timestamps, device model, and device IDs for physical devices connected to the machine, resolving a duplicate-timestamp edge case by selecting the earliest entry as the true connection event.
5. **Web activity reconstruction** — Filtered the Web History artifact to a specific date range and isolated search-engine queries by parsing search text out of the visited URLs.
6. **Software installation timeline** — Used the **Installed Programs** registry artifact viewer, sorted and filtered by install date, to build a timeline of software installed within a target window.
7. **Unique media identification** — Used the File Types viewer (sorted by extension, filtered to Video) and compared file paths to distinguish user-generated personal media from OS/application/cache video files.
8. **PII handling** — Catalogued every category of PII encountered during the investigation (account identifiers, email address, search history, device serial numbers) and applied the ACS Code of Ethics — specifically public interest, honesty, and professional integrity — to determine that unrelated PII should be documented at a category level, segregated, and never copied or analysed beyond what's necessary for the case.

## Key Findings (Generalised)
- One primary non-system user account was identified, with a low-but-nonzero login count, standard (non-admin) privilege level, and a password policy that didn't enforce expiry — a notable finding from a security-hygiene perspective.
- A third-party messaging client was found to have been installed and used within the same week the account was created, identified entirely through filesystem artifacts rather than direct evidence of app usage.
- Two classes of physical devices (a mobile phone and a USB flash drive) had connected to the machine, recoverable via registry USB artifacts even without the physical devices present.
- Search history within the target window showed escalating concern-driven queries (e.g. researching whether the device had been compromised), useful for building an incident timeline.
- A short, defined software-install window revealed a mix of routine driver/runtime updates and a notable network-virtualisation tool — relevant context for any incident-response read of the timeline.
- Of all video files on the disk, only one was determined to be user-generated personal content; the rest were system, application, or cache artifacts — distinguished purely by file path heuristics.

## Ethical Considerations
Applied the **Australian Computer Society (ACS) Code of Ethics** to PII encountered outside the scope of the investigation:
- **Minimisation & segregation** — unrelated PII documented by category, not content; isolated from analysis
- **Transparency & honesty** — discovery logged in case notes without recording the sensitive data itself
- **Legal compliance** — handling aligned with Privacy Act 1988 obligations, escalated to legal authority only where required

## Skills Demonstrated
- Digital forensic investigation & Windows artifact analysis
- Chain of custody and evidence integrity assessment
- Registry artifact analysis (USB history, installed programs, OS accounts)
- Web history / search reconstruction
- File system and metadata analysis
- PII identification and ethical handling
- Technical investigation reporting

## What I Learned
This project deepened my understanding of how forensic investigators move from raw disk artifacts to a defensible, well-documented narrative — and how every step (a registry key, a folder timestamp, a missing hash) either strengthens or weakens the integrity of the evidence chain. It also sharpened my ability to reason about privacy obligations in real time, rather than as an afterthought to the technical work.

## Important Note
This repository does not include the original forensic disk image, any source material, screenshots containing personal information, or restricted material. Identifying details (account names, email addresses, device serial numbers) have been generalised or omitted. This is a cleaned, anonymised project summary for portfolio purposes only.
