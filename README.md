# Discourse custom emoji icons

A deduplicated collection of image assets arranged into upload-ready groups for [`dsc`](https://github.com/pacharanero/dsc). This repository was consolidated from two copies of the same Git history on 27 July 2026; every retained asset has a unique content hash and filename stem.

## Upload-ready groups

`dsc` uploads image files in the specified directory but does not recurse into child directories. Pass one leaf directory at a time.

| Directory | Files | Intended use |
| --- | ---: | --- |
| `upload-ready/discourse-ui/` | 76 | Generic navigation, editing, status, and interaction symbols |
| `upload-ready/general/` | 4 | General-purpose visual reactions |
| `upload-ready/healthcare-accessibility/` | 6 | Healthcare and accessibility symbols |
| `upload-ready/linux-tech/` | 37 | Operating systems, programming, and open-source technology |
| `upload-ready/places/` | 6 | Flags and regional symbols |
| `upload-ready/service-providers/` | 21 | Hosting, cloud, productivity, email, and platform brands |
| `upload-ready/socials/` | 10 | Social and messaging services |
| `upload-ready/organisations/govuk/` | 2 | GOV.UK crown variants |
| `upload-ready/organisations/igkt/` | 1 | International Guild of Knot Tyers |
| `upload-ready/organisations/nhs/` | 1 | NHS |
| `upload-ready/organisations/pmpc/` | 1 | Public Money Public Code |
| `upload-ready/organisations/rcpch/` | 6 | RCPCH and RCPCH Incubator variants |
| `upload-ready/organisations/restorative-just-culture/` | 1 | Restorative Just Culture Community of Practice |
| `upload-ready/organisations/rhyl-fold-farm/` | 2 | Rhyl Fold Farm variants |

Do not pass `upload-ready/organisations/` itself because its assets are in child directories.

## Using `dsc`

Review the selected leaf directory and the forum's existing custom emoji, then apply:

```console
dsc emoji list <forum>
dsc emoji push <forum> ./upload-ready/socials
```

`emoji add` is an alias for `emoji push`. The filename stem becomes the Discourse emoji name. Stems are globally unique across `upload-ready/`, so several groups can be installed on one forum without this repository creating name collisions. Existing remote emoji may still use the same names, so inspect the current forum state first.

As of `dsc` 0.10.30, `emoji push --dry-run` refuses safely because a complete upload plan has not yet been implemented. Recheck the installed command's help and behaviour in later versions rather than assuming this limitation still applies.

Credentials remain in the normal `dsc.toml` configuration. Do not add API keys or per-forum environment files to this asset repository.

## Font Awesome Free

`fontawesome-free-6.7.2-web/` is one complete, extracted upstream Font Awesome Free distribution. It remains outside `upload-ready/` because it is a large vendor collection rather than a curated forum set.

Individual style directories are directly uploadable, for example:

```console
dsc emoji push <forum> ./fontawesome-free-6.7.2-web/svgs/solid
```

Regular, solid, and brand sets can contain identical filename stems. Select the style you want rather than uploading every style directory indiscriminately. Retain the upstream `LICENSE.txt` and observe Font Awesome's licensing and attribution requirements.

## Asset provenance and use

- Organisation logos are grouped separately because they are generally appropriate only for the organisation that owns them.
- Service and social-media marks may be subject to brand-usage rules even when the files are technically reusable.
- Historical brands are retained when they are unique, but their presence does not imply that they are current.
- Two unusable files were deliberately excluded during consolidation: a transparent SVG with a broken viewport and a supposed transparent Yorkshire rose containing an opaque checkerboard. Two copied Font Awesome files were replaced by the equivalent assets in the complete Free distribution.

The obsolete Python uploader was intentionally removed in the repository's existing history because it created orphan Discourse uploads rather than Custom Emoji records. Use `dsc emoji push` instead.
