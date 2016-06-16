"""Extra default config sections from pkgcheck."""

from pkgcore.config import basics

from .. import base

pkgcore_plugins = {
    'global_config': [{
        'package-and-ver': basics.ConfigSectionFromStringDict({
            'class': 'pkgcheck.base.Scope',
            'scopes': ' '.join((str(base.package_scope),
                                str(base.version_scope))),
            }),
        'non-repo': basics.ConfigSectionFromStringDict({
            'class': 'pkgcheck.base.Scope',
            'scopes': ' '.join((str(base.package_scope), str(base.category_scope),
                                str(base.version_scope))),
            }),
        'repo-category': basics.ConfigSectionFromStringDict({
            'class': 'pkgcheck.base.Scope',
            'scopes': ' '.join((str(base.repository_scope), str(base.category_scope))),
            }),
        'repo': basics.ConfigSectionFromStringDict({
            'class': 'pkgcheck.base.Scope',
            'scopes': str(base.repository_scope),
            }),
        'no-arch': basics.ConfigSectionFromStringDict({
            'class': 'pkgcheck.base.Blacklist',
            'patterns': 'unstable_only stale_unstable imlate',
            }),
        'all': basics.ConfigSectionFromStringDict({
            'class': 'pkgcheck.base.Blacklist',
            'patterns': '',
            }),
        }],
    }
