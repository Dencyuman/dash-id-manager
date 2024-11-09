# Dash ID Manager

A Python library for efficient and scalable ID management in Plotly Dash applications using dataclasses. Simplify and standardize the way you handle component IDs, enhancing maintainability, reducing errors, and improving developer experience.

## README Language
[日本語版](https://github.com/Dencyuman/dash-id-manager/blob/main/docs/README_ja.md)

## Features

- **Hierarchical ID Grouping**: Use dataclasses to group IDs hierarchically, reflecting the structure of your Dash application.
- **Automatic Prefix Insertion**: Automatically inserts prefixes based on the class hierarchy, indicating the page and component hierarchy.
- **Centralized ID Management**: Define all IDs in a single location (e.g., `__init__.py`), making ID management consistent and maintainable across the entire project.
- **Enhanced Error Reporting**: When errors occur, it's clear which page and component the ID belongs to, facilitating easier debugging.
- **Improved Editor Support**: Leverage editor indexing and autocomplete features for faster development and reduced type errors.
- **Declarative ID Definitions**: Manage IDs declaratively using dataclasses, reducing boilerplate and improving readability.
- **Automatic Kebab-Case Conversion**: Automatically converts field names to kebab-case for consistent ID formatting without additional code.
- **Immutable and Type-Safe**: Utilizes frozen dataclasses to ensure ID integrity and prevent accidental modifications.

## Installation

You can install the library via pip:

```bash
pip install dash-id-manager
```

## Usage
Here's an advanced example demonstrating how to efficiently manage IDs using Dash ID Manager in your Dash application:

```python
# __init__.py
from dash_id_manager import PageIDs, ComponentIDs
from dataclasses import dataclass
from typing import ClassVar

@dataclass(frozen=True)
class DashboardIDs(PageIDs):
    _prefix: ClassVar[str] = "dashboard"

    header: 'DashboardHeaderIDs'
    sidebar: 'DashboardSidebarIDs'
    content: 'DashboardContentIDs'

@dataclass(frozen=True)
class DashboardHeaderIDs(ComponentIDs):
    _prefix: ClassVar[str] = "header"

    title: str
    logout_button: str

@dataclass(frozen=True)
class DashboardSidebarIDs(ComponentIDs):
    _prefix: ClassVar[str] = "sidebar"

    navigation_menu: str
    profile_section: str

@dataclass(frozen=True)
class DashboardContentIDs(ComponentIDs):
    _prefix: ClassVar[str] = "content"

    graph: str
    data_table: str

# Initialize all ID groups
header_ids = DashboardHeaderIDs()
sidebar_ids = DashboardSidebarIDs()
content_ids = DashboardContentIDs()

# Usage in app.py
import dash
from dash import html, dcc

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Header([
        html.H1(id=header_ids.title),  # id = "dashboard-header-title"
        html.Button("Logout", id=header_ids.logout_button)  # id = "dashboard-header-logout-button"
    ], id=header_ids._prefix),  # id = "dashboard-header"

    html.Aside([
        html.Nav(id=sidebar_ids.navigation_menu),  # id = "dashboard-sidebar-navigation-menu"
        html.Div(id=sidebar_ids.profile_section)  # id = "dashboard-sidebar-profile-section"
    ], id=sidebar_ids._prefix),  # id = "dashboard-sidebar"

    html.Main([
        dcc.Graph(id=content_ids.graph),  # id = "dashboard-content-graph"
        html.Table(id=content_ids.data_table)  # id = "dashboard-content-data-table"
    ], id=content_ids._prefix)  # id = "dashboard-content"
])

if __name__ == '__main__':
    app.run_server(debug=True)
```

## Demonstrated Advantages

- **Hierarchical Grouping**: `DashboardIDs` groups all related component IDs, reflecting the structure of the page.
- **Automatic Prefixing**: Each subclass (e.g., `DashboardHeaderIDs`, `DashboardSidebarIDs`) automatically inherits the parent prefix, generating IDs like `dashboard-header-title`.
- **Centralized Management**: All IDs are defined in `__init__.py`, making them easily accessible and modifiable. Of course, they can be split into other files as well.
- **Improved Error Reporting**: Structured naming ensures that when ID-related errors occur, the affected pages or components are clearly identified.
- **Editor Support**: IDEs can autocomplete entries like `dashboard_ids.header.title`, reducing the possibility of typos.
- **Declarative Definitions**: Using data classes to declaratively define IDs makes the code cleaner and easier to maintain.
- **Automatic Kebab-Case Conversion**: Field names like `logout_button` are automatically converted to `logout-button`, ensuring consistent ID formatting.
- **Immutable IDs**: Using frozen data classes maintains the integrity of IDs by preventing runtime changes.


## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE.md) file for details.
