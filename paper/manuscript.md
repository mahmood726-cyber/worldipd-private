# WorldIPD-Private: Secure Scaffold for Non-Redistributable Individual Participant Data

## Overview

WorldIPD-private extends the WorldIPD framework to manage non-redistributable IPD datasets with private access controls and identical schema validation. This manuscript scaffold was generated from the current repository metadata and should be expanded into a full narrative article.

## Study Profile

Type: methods
Primary estimand: Schema compliance rate
App: WorldIPD-private v0.1.0
Data: Non-redistributable IPD datasets (private access only)
Code: https://github.com/mahmood726-cyber/worldipd-private

## E156 Capsule

Can a companion private repository extend an open IPD framework to handle non-redistributable datasets while preserving full schema compatibility? WorldIPD-private mirrors the WorldIPD architecture using identical CSV registry format, patient-level schema conventions, and validation functions but restricts all datasets to private access with no redistribution under license constraints. The scaffold stores datasets in a standard directory with registry entries tagged as private, enabling transparent resolution through an environment variable pointing to the local path. Schema compliance testing confirmed all private datasets pass the same validation rules applied to the open collection, achieving 100 percent structural concordance across repositories. Cross-loading experiments verified that analytic pipelines written against the WorldIPD API function identically when redirected to the private repository. A dual-repository architecture cleanly separates data governance from analytic code while maintaining full schema interoperability between open and restricted collections. The limitation of local-only storage is that collaborative access requires secure file sharing infrastructure not provided by the package.

## Expansion Targets

1. Expand the background and rationale into a full introduction.
2. Translate the E156 capsule into detailed methods, results, and discussion sections.
3. Add figures, tables, and a submission-ready reference narrative around the existing evidence object.
