# Repositories summary

Here you can find a list of all First Asset repositories and their purpose

## Products

The next repositories are products that our users use in day-to-day work:

| Name                                                                       | Description                |
| -------------------------------------------------------------------------- | -------------------------------- |
| :point_up: [Succession Risk Planning (succession-planning)][srm-repo]      | ![][srm-readme] ![][srm-tests] ![][srm-gha] ![][local-ci-on] <br> Allows to manage and prepare successors for a particular position in a company |
| :point_up: [Budget Allocation Tool (batman)][bat-repo]                     | ![][bat-readme] ![][bat-tests] ![][bat-gha] ![][local-ci-on] <br>Allows to manage and distribute budget and bonuses across company        |
| :point_up: [topexec (topexec)][topexec-repo]                               | ![][topexec-readme] ![][topexec-tests] ![][topexec-gha] ![][local-ci-off] <br> **Unknown**                                                       |
| :point_up: [CEO Special Allocations(ceosa)][ceosa-repo]                    | ![][ceosa-readme] ![][ceosa-tests] ![][ceosa-gha] ![][local-ci-off] <br> **Unknown**                                                       |


[srm-repo]: https://github.com/firstassethr/succession-planning
[srm-readme]: https://img.shields.io/badge/README-7-green
[srm-tests]: https://img.shields.io/badge/Tests-3-red
[srm-gha]: https://github.com/firstassethr/succession-planning/actions/workflows/validate.yml/badge.svg

[bat-repo]: https://github.com/firstassethr/batman
[bat-readme]: https://img.shields.io/badge/README-5-yellow
[bat-tests]: https://img.shields.io/badge/Tests-3-red
[bat-gha]: https://github.com/firstassethr/batman/actions/workflows/validate.yml/badge.svg

[topexec-repo]: https://github.com/firstassethr/topexec
[topexec-readme]: https://img.shields.io/badge/README-0-red
[topexec-tests]: https://img.shields.io/badge/Tests-0-red
[topexec-gha]: https://img.shields.io/badge/Validate%20Prs-No-red

[ceosa-repo]: https://github.com/firstassethr/ceosa
[ceosa-readme]: https://img.shields.io/badge/README-3-red
[ceosa-tests]: https://img.shields.io/badge/Tests-0-red
[ceosa-gha]: https://github.com/firstassethr/ceosa/actions/workflows/validate.yml/badge.svg

## Production Libraries

| Name                                                    | Description                                                      |
| ------------------------------------------------------- | ---------------------------------------------------------------------- |
| :point_up: [morpheus][morpheus-repo]                    | ![][morpheus-readme] ![][morpheus-tests] ![][morpheus-gha] ![][local-ci-on] <br> Custom [DAL] for all apps, on top of [postgres.js] and [ucast]         |
| :point_up: [dataloader][dataloader-repo]                | ![][dataloader-readme] ![][dataloader-tests] ![][dataloader-gha] ![][local-ci-on] <br> Dataloaders configured to serve the purpose of in-memory Application Cache           |
| :point_up: [tokens-store][token-store-repo]             | ![][token-store-readme] ![][token-store-tests] ![][token-store-gha] ![][local-ci-on] <br> Token store app service to handle common authentication scenarios on backend   |
| :point_up: [config][config-repo]                        | ![][config-readme] ![][config-tests] ![][config-gha] ![][local-ci-on] <br> Config based on JSON5 and explicit inheritance                                 |
| :point_up: [node-server][server-repo]                   | ![][server-readme] ![][server-tests] ![][server-gha] ![][local-ci-on] <br> Platform level repository that provides common server configuration and utilities, like Distributed Dataloader's Cache |
| :point_up: [oscar][oscar-repo]                          | ![][oscar-readme] ![][oscar-tests] ![][oscar-gha-client] ![][oscar-gha-server] ![][local-ci-off] <br>HTML to PDF convertor, uses [playwright] and Google Chrome browser |
| :point_up: [app-uisession][uisession-repo]              | ![][uisession-readme] ![][uisession-tests] ![][uisession-gha] ![][local-ci-on] <br> Tracks user's idle state and session expiration on frontend  |
| :point_up: [fahr-apollo-client][apollo-repo]            | ![][apollo-readme] ![][apollo-tests] ![][apollo-gha] ![][local-ci-on] <br> Apollo client factory with preconfigured links, shared across all First Asset apps |
| :point_up: [treeoflife][treeoflife-repo]                | ![][treeoflife-readme] ![][treeoflife-tests] ![][treeoflife-gha] ![][local-ci-on] <br> Org Tree stuff |
| [secretbox][secretbox-repo]                             | ![][secretbox-readme] ![][secretbox-tests] ![][secretbox-gha] ![][local-ci-on] <br> Universal encryption/decryption (Node, browser, web/service workers, CloudFlare workers) |
| [fahr-emailer][mailer-repo]                             | ![][mailer-readme] ![][mailer-tests] ![][mailer-gha] ![][local-ci-on] <br> mailer service on top of [nodemailer] |
| [Excel][excel-repo]                                     | ![][excel-readme] ![][excel-tests] ![][excel-gha] ![][local-ci-on] <br> Preconfigured excel service that allows to parse excel file (usually to import data in database) |
| [livelink][livelink-repo]                               | ![][livelink-readme] ![][livelink-tests] ![][livelink-gha] ![][local-ci-off] <br> A universal library (works on the server and on the client) to establish a two-way connection between "backend" and "frontend" via WebSockets. |
| [graphql-guid][gql-guid-repo]                           | ![][gql-guid-readme] ![][gql-guid-tests] ![][gql-guid-gha] ![][local-ci-off] <br> GraphQL GUID scalar that encrypts entity type and id of all primary and foreign keys |
| [emitter][emitter-repo]                                 | ![][emitter-readme] ![][emitter-tests] ![][emitter-gha] ![][local-ci-off] <br> Universal, TypeScript-safe, minimal EventEmitter for FA projects               |

[morpheus-repo]: https://github.com/firstassethr/morpheus
[morpheus-readme]: https://img.shields.io/badge/README-9-green
[morpheus-tests]: https://img.shields.io/badge/Tests-9-green
[morpheus-gha]: https://github.com/firstassethr/morpheus/actions/workflows/validate.yml/badge.svg

[dataloader-repo]: https://github.com/firstassethr/dataloader
[dataloader-readme]: https://img.shields.io/badge/README-0-red
[dataloader-tests]: https://img.shields.io/badge/Tests-7-green
[dataloader-gha]: https://github.com/firstassethr/dataloader/actions/workflows/validate.yml/badge.svg

[token-store-repo]: https://github.com/firstassethr/tokens-store
[token-store-readme]: https://img.shields.io/badge/README-5-yellow
[token-store-tests]: https://img.shields.io/badge/Tests-10-green
[token-store-gha]: https://github.com/firstassethr/tokens-store/actions/workflows/validate.yml/badge.svg

[config-repo]: https://github.com/firstassethr/config
[config-readme]: https://img.shields.io/badge/README-0-red
[config-tests]: https://img.shields.io/badge/Tests-9-green
[config-gha]: https://github.com/firstassethr/config/actions/workflows/validate.yml/badge.svg

[server-repo]: https://github.com/firstassethr/node-server
[server-readme]: https://img.shields.io/badge/README-5-yellow
[server-tests]: https://img.shields.io/badge/Tests-5-yellow
[server-gha]: https://github.com/firstassethr/node-server/actions/workflows/validate.yml/badge.svg

[oscar-repo]: https://github.com/firstassethr/oscar
[oscar-readme]: https://img.shields.io/badge/README-7-green
[oscar-tests]: https://img.shields.io/badge/Tests-8-green
[oscar-gha-client]: https://github.com/firstassethr/oscar/workflows/Validate%20oscar-client/badge.svg
[oscar-gha-server]: https://github.com/firstassethr/oscar/workflows/Validate%20oscar-server/badge.svg

[uisession-repo]: https://github.com/firstassethr/app-uisession
[uisession-readme]: https://img.shields.io/badge/README-7-green
[uisession-tests]: https://img.shields.io/badge/Tests-5-yellow
[uisession-gha]: https://github.com/firstassethr/app-uisession/actions/workflows/validate.yml/badge.svg

[apollo-repo]: https://github.com/firstassethr/fahr-apollo-client
[apollo-readme]: https://img.shields.io/badge/README-5-yellow
[apollo-tests]: https://img.shields.io/badge/Tests-5-yellow
[apollo-gha]: https://github.com/firstassethr/fahr-apollo-client/actions/workflows/validate.yml/badge.svg

[treeoflife-repo]: https://github.com/firstassethr/treeoflife
[treeoflife-readme]: https://img.shields.io/badge/README-0-red
[treeoflife-tests]: https://img.shields.io/badge/Tests-8-green
[treeoflife-gha]: https://github.com/firstassethr/treeoflife/actions/workflows/validate.yml/badge.svg

[secretbox-repo]: https://github.com/firstassethr/secretbox
[secretbox-readme]: https://img.shields.io/badge/README-1-red
[secretbox-tests]: https://img.shields.io/badge/Tests-5-yellow
[secretbox-gha]: https://github.com/firstassethr/secretbox/actions/workflows/validate.yml/badge.svg

[mailer-repo]: https://github.com/firstassethr/fahr-emailer
[mailer-readme]: https://img.shields.io/badge/README-5-yellow
[mailer-tests]: https://img.shields.io/badge/Tests-7-green
[mailer-gha]: https://github.com/firstassethr/fahr-emailer/actions/workflows/validate-prs.yml/badge.svg

[excel-repo]: https://github.com/firstassethr/excel
[excel-readme]: https://img.shields.io/badge/README-0-red
[excel-tests]: https://img.shields.io/badge/Tests-7-green
[excel-gha]: https://github.com/firstassethr/excel/actions/workflows/validate.yml/badge.svg

[livelink-repo]: https://github.com/firstassethr/livelink
[livelink-readme]: https://img.shields.io/badge/README-0-red
[livelink-tests]: https://img.shields.io/badge/Tests-5-yellow
[livelink-gha]: https://github.com/firstassethr/livelink/actions/workflows/validate.yml/badge.svg

[gql-guid-repo]: https://github.com/firstassethr/graphql-guid
[gql-guid-readme]: https://img.shields.io/badge/README-0-red
[gql-guid-tests]: https://img.shields.io/badge/Tests-8-green
[gql-guid-gha]: https://github.com/firstassethr/graphql-guid/actions/workflows/validate.yml/badge.svg

[emitter-repo]: https://github.com/firstassethr/emitter
[emitter-readme]: https://img.shields.io/badge/README-0-red
[emitter-tests]: https://img.shields.io/badge/Tests-5-yellow
[emitter-gha]: https://github.com/firstassethr/emitter/actions/workflows/validate.yml/badge.svg

[nodemailer]: https://github.com/nodemailer/nodemailer
[playwright]: https://playwright.dev/
[DAL]: https://en.wikipedia.org/wiki/Data_access_layer
[postgres.js]: https://github.com/porsager/postgres
[ucast]: https://github.com/stalniy/ucast

## Client System Integrations

| Name                                         | Description                |
| -------------------------------------------- | -------------------------------- |
| [oauth-server][oauth-server-repo]            | ![][oauth-server-readme] ![][oauth-server-tests] ![][oauth-server-gha] ![][local-ci-on] <br> A central OAuth server to handle SSO needs across First Asset |
| [visionproxy][vision-proxy-repo]             | ![][vision-proxy-readme] ![][vision-proxy-tests] ![][vision-proxy-gha] ![][local-ci-off] <br> Contextually fetching photos for different apps |
| [sag-photo-worker][sag-photo-repo]           | ![][sag-photo-readme] ![][sag-photo-tests] ![][sag-photo-gha] ![][local-ci-off] <br> Cloudflare Worker to act as an edge CDN/proxy for the Vision photo API |
| [sag-api-scd][sag-scd-repo]                  | ![][sag-scd-readme] ![][sag-scd-tests] ![][sag-scd-gha] ![][local-ci-off] <br> API library for searching Siemens SCD system |
| [siemens-webservice-maindata][swm-repo]      | ![][swm-readme] ![][swm-tests] ![][swm-gha] ![][local-ci-on] <br> The public API to exchange data with Siemens Group of companies |


[oauth-server-repo]: https://github.com/firstassethr/oauth-server
[oauth-server-readme]: https://img.shields.io/badge/README-3-red
[oauth-server-tests]: https://img.shields.io/badge/Tests-7-green
[oauth-server-gha]: https://github.com/firstassethr/oauth-server/workflows/Validate%20code/badge.svg

[vision-proxy-repo]: https://github.com/firstassethr/visionproxy
[vision-proxy-readme]: https://img.shields.io/badge/README-0-red
[vision-proxy-tests]: https://img.shields.io/badge/Tests-5-yellow
[vision-proxy-gha]: https://github.com/firstassethr/visionproxy/actions/workflows/build-and-reease.yml/badge.svg

[sag-photo-repo]: https://github.com/firstassethr/sag-photo-worker
[sag-photo-readme]: https://img.shields.io/badge/README-5-yellow
[sag-photo-tests]: https://img.shields.io/badge/Tests-0-red
[sag-photo-gha]: https://github.com/firstassethr/sag-photo-worker/actions/workflows/validate.yml/badge.svg

[sag-scd-repo]: https://github.com/firstassethr/sag-api-scd
[sag-scd-readme]: https://img.shields.io/badge/README-3-red
[sag-scd-tests]: https://img.shields.io/badge/Tests-0-red
[sag-scd-gha]: https://github.com/firstassethr/sag-api-scd/actions/workflows/validate.yml/badge.svg

[swm-repo]: https://github.com/firstassethr/siemens-webservice-maindata
[swm-readme]: https://img.shields.io/badge/README-5-yellow
[swm-tests]: https://img.shields.io/badge/Tests-4-yellow
[swm-gha]: https://github.com/firstassethr/siemens-webservice-maindata/actions/workflows/validate.yml/badge.svg

## Development Libraries

| Name                                         | Short Description                |
| -------------------------------------------- | -------------------------------- |
| :point_up: [frontbuild][frontbuild-repo]     | ![][frontbuild-readme] ![][frontbuild-tests] ![][frontbuild-gha] ![][local-ci-on] <br> Custom configuration of [rollup] and [vite] to build First Asset UI |
| :point_up: [local-ci][local-ci-repo]         | ![][local-ci-readme] ![][local-ci-tests] ![][local-ci-gha] ![][local-ci-on] <br> Proxy CLI over common node development tools that provides default configuration for prettier, eslint, semantic-release, local git hooks, etc |
| [graphql-vcr][graphql-vcr-repo]              | ![][graphql-vcr-readme] ![][graphql-vcr-tests] ![][graphql-vcr-gha] ![][local-ci-on] <br> [jest] adoption for testing GraphQL APIs using snapshots and playbooks |
| [jest-preset][jest-preset-repo]              | ![][jest-preset-readme] ![][jest-preset-tests] ![][jest-preset-gha] ![][local-ci-on] <br> Preconfigured [jest] preset for all First Asset repositories |
| [eslint-plugin][eslint-plugin-repo]          | ![][eslint-plugin-readme] ![][eslint-plugin-tests] ![][eslint-plugin-gha] ![][local-ci-off] <br> Custom configuration of [eslint] rules for all First Asset repos |
| [tsconfig][tsconfig-repo]                    | ![][tsconfig-readme] ![][tsconfig-tests] ![][tsconfig-gha] ![][local-ci-off] <br> Preconfigured [TypeScript] config for all First Asset repositories: apps, ui and api libs |
| [tsrequire][tsrequire-repo]                  | ![][tsrequire-readme] ![][tsrequire-tests] ![][tsrequire-gha] ![][local-ci-on] <br> Alternative to `ts-node/register` without type checks and super-fast server build/reload thanks to [esbuild] |


[frontbuild-repo]: https://github.com/firstassethr/frontbuild
[frontbuild-readme]: https://img.shields.io/badge/README-3-red
[frontbuild-tests]: https://img.shields.io/badge/Tests-8-green
[frontbuild-gha]: https://github.com/firstassethr/frontbuild/actions/workflows/validate.yml/badge.svg

[graphql-vcr-repo]: https://github.com/firstassethr/graphql-vcr
[graphql-vcr-readme]: https://img.shields.io/badge/README-7-green
[graphql-vcr-tests]: https://img.shields.io/badge/Tests-5-yellow
[graphql-vcr-gha]: https://github.com/firstassethr/graphql-vcr/actions/workflows/validate.yml/badge.svg

[local-ci-repo]: https://github.com/firstassethr/local-ci
[local-ci-readme]: https://img.shields.io/badge/README-7-green
[local-ci-tests]: https://img.shields.io/badge/Tests-5-yellow
[local-ci-gha]: https://github.com/firstassethr/local-ci/actions/workflows/validate.yml/badge.svg

[jest-preset-repo]: https://github.com/firstassethr/jest-preset
[jest-preset-readme]: https://img.shields.io/badge/README-7-green
[jest-preset-tests]: https://img.shields.io/badge/Tests-7-green
[jest-preset-gha]: https://github.com/firstassethr/jest-preset/actions/workflows/validate.yml/badge.svg

[eslint-plugin-repo]: https://github.com/firstassethr/eslint-plugin
[eslint-plugin-readme]: https://img.shields.io/badge/README-5-yellow
[eslint-plugin-tests]: https://img.shields.io/badge/Tests-8-green
[eslint-plugin-gha]: https://github.com/firstassethr/eslint-plugin/workflows/Validate%20code/badge.svg

[tsconfig-repo]: https://github.com/firstassethr/tsconfig
[tsconfig-readme]: https://img.shields.io/badge/README-5-yellow
[tsconfig-tests]: https://img.shields.io/badge/Tests-9-green
[tsconfig-gha]: https://github.com/firstassethr/tsconfig/actions/workflows/validate.yml/badge.svg

[tsrequire-repo]: https://github.com/firstassethr/tsrequire
[tsrequire-readme]: https://img.shields.io/badge/README-9-green
[tsrequire-tests]: https://img.shields.io/badge/Tests-7-green
[tsrequire-gha]: https://github.com/firstassethr/tsrequire/actions/workflows/validate.yml/badge.svg

[eslint]: https://eslint.org/
[esbuild]: https://github.com/evanw/esbuild
[rollup]: https://rollupjs.org/
[vite]: https://vitejs.dev/
[jest]: https://jestjs.io/
[TypeScript]: https://www.typescriptlang.org/


## Infrastructure related

| Name                                         | Short Description                |
| -------------------------------------------- | -------------------------------- |
| [appdeploy][appdeploy-repo]                  | ![][appdeploy-readme] ![][appdeploy-tests] ![][appdeploy-gha] ![][local-ci-on] <br> Installs applications (BAT/SRM/CEOSA/TopExec) on the production server                      |
| [dbbackup][dbbackup-repo]                    | ![][dbbackup-readme] ![][dbbackup-tests] ![][dbbackup-gha] ![][local-ci-off] <br> **Unknown**                      |
| [Github Action tools (gha)][gha-repo]        | ![][gha-readme] ![][gha-tests] ![][gha-gha] ![][local-ci-off] <br> Reusable utility for github actions: node_modules autocache, private node registry token configuration  |
| [renovate-config][renovate-config-repo]      | ![][renovate-config-readme] ![][renovate-config-tests] ![][renovate-config-gha] <br> Configuration for [renovate] |
| [aws-s3][awss3-repo]        | ![][awss3-readme] ![][awss3-tests] ![][awss3-gha] ![][local-ci-on] <br> High level client to AWS S3 |


[appdeploy-repo]: https://github.com/firstassethr/appdeploy
[appdeploy-readme]: https://img.shields.io/badge/README-1-yellow
[appdeploy-tests]: https://img.shields.io/badge/Tests-1-yellow
[appdeploy-gha]:  https://github.com/firstassethr/appdeploy/workflows/Validate%20code/badge.svg

[dbbackup-repo]: https://github.com/firstassethr/dbbackup
[dbbackup-readme]: https://img.shields.io/badge/README-5-yellow
[dbbackup-tests]: https://img.shields.io/badge/Tests-0-red
[dbbackup-gha]:  https://img.shields.io/badge/Validate%20Prs-No-red

[gha-repo]: https://github.com/firstassethr/gha
[gha-readme]: https://img.shields.io/badge/README-7-green
[gha-tests]: https://img.shields.io/badge/Tests-1-green
[gha-gha]: https://github.com/firstassethr/gha/workflows/Validate%20code/badge.svg

[renovate-config-repo]: https://github.com/firstassethr/renovate-config
[renovate-config-readme]: https://img.shields.io/badge/README-1-green
[renovate-config-tests]: https://img.shields.io/badge/Tests-1-green
[renovate-config-gha]: https://github.com/firstassethr/renovate-config/actions/workflows/validate.yml/badge.svg

[awss3-repo]: https://github.com/firstassethr/aws-s3
[awss3-readme]: https://img.shields.io/badge/README-1-yellow
[awss3-tests]: https://img.shields.io/badge/Tests-5-green
[awss3-gha]: https://github.com/firstassethr/aws-s3/workflows/Validate%20code/badge.svg


[renovate]: https://www.whitesourcesoftware.com/free-developer-tools/renovate/

## Templates

| Name                                         | Short Description                |
| -------------------------------------------- | -------------------------------- |
| [playground-serverlib][serverlib-repo]       |  ![][serverlib-readme] ![][serverlib-gha] ![][local-ci-on] <br> Template for backend libraries with preconfigured defaults and development dependencies |



[serverlib-repo]: https://github.com/firstassethr/playground-serverlib
[serverlib-readme]: https://img.shields.io/badge/README-7-green
[serverlib-gha]: https://github.com/firstassethr/playground-serverlib/workflows/Validate%20code/badge.svg


## Incubating

| Name          | Short Description                |
| ------------- | -------------------------------- |
| [adobepdf][adobepdf-repo]       |  ![][adobepdf-readme] ![][adobepdf-gha] ![][local-ci-on] <br> Used for converting DOCX documents to PDF Acts like a good netizen by limiting concurrent and overall requests |

[adobepdf-repo]: https://github.com/firstassethr/adobepdf
[adobepdf-readme]: https://img.shields.io/badge/README-1-green
[adobepdf-gha]: https://github.com/firstassethr/adobepdf/workflows/Validate%20code/badge.svg



## Legacy

| Name                                         | Short Description                |
| -------------------------------------------- | -------------------------------- |
| [PG client][pgclient-repo]                   | [PostgreSQL] Client for First Asset HR projects. Old DAL for First Asset apps. Replaced by [Morpheus][morpheus-repo] |
| [Webpack Factory][webpack-factory-repo]      | Preconfigured [webpack] configuration. Replaced by [Front build][frontbuild-repo] |
| [UI Kit][uikit-repo]                         | UI components used accross FAHR apps. Abandoned |
| [Secret][secret-repo]                        | Pass secrets between FA applications over cleartext. Replaced by [Secretbox][secretbox-repo] |


[pgclient-repo]: https://github.com/firstassethr/pg-client
[webpack-factory-repo]: https://github.com/firstassethr/webpack-factory
[uikit-repo]: https://github.com/firstassethr/ui-kit
[secret-repo]: https://github.com/firstassethr/secret

[webpack]: https://webpack.js.org/
[PostgreSQL]: https://www.postgresql.org/

[local-ci-on]: https://img.shields.io/badge/local--ci-on-green
[local-ci-off]: https://img.shields.io/badge/local--ci-off-red
