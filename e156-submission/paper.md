Mahmood Ahmad
Tahir Heart Institute
mahmood.ahmad2@nhs.net

WorldIPD-Private: Secure Scaffold for Non-Redistributable Individual Participant Data

Can a companion private repository extend an open IPD framework to handle non-redistributable datasets while preserving full schema compatibility? WorldIPD-private mirrors the WorldIPD architecture using identical CSV registry format, patient-level schema conventions, and validation functions but restricts all datasets to private access with no redistribution under license constraints. The scaffold stores datasets in a standard directory with registry entries tagged as private, enabling transparent resolution through an environment variable pointing to the local path. Schema compliance testing confirmed all private datasets pass the same validation rules applied to the open collection, achieving 100 percent structural concordance across repositories. Cross-loading experiments verified that analytic pipelines written against the WorldIPD API function identically when redirected to the private repository. A dual-repository architecture cleanly separates data governance from analytic code while maintaining full schema interoperability between open and restricted collections. The limitation of local-only storage is that collaborative access requires secure file sharing infrastructure not provided by the package.

Outside Notes

Type: methods
Primary estimand: Schema compliance rate
App: WorldIPD-private v0.1.0
Data: Non-redistributable IPD datasets (private access only)
Code: https://github.com/mahmood726-cyber/worldipd-private
Version: 0.1.0
Validation: DRAFT

References

1. Borenstein M, Hedges LV, Higgins JPT, Rothstein HR. Introduction to Meta-Analysis. 2nd ed. Wiley; 2021.
2. Higgins JPT, Thompson SG, Deeks JJ, Altman DG. Measuring inconsistency in meta-analyses. BMJ. 2003;327(7414):557-560.
3. Cochrane Handbook for Systematic Reviews of Interventions. Version 6.4. Cochrane; 2023.
