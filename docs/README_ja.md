# Dash ID Manager
Plotly DashアプリケーションにおけるID管理を効率的かつスケーラブルに行うためのPythonライブラリです。データクラスを使用してコンポーネントIDの管理を簡素化・標準化し、保守性の向上、エラーの削減、開発者体験の向上を実現します。

## 特徴
- **階層的なIDグルーピング**: データクラスを使用してIDを階層的にグループ化し、Dashアプリケーションの構造を反映します。
- **自動プレフィックス挿入**: クラス階層に基づいてプレフィックスを自動的に挿入し、ページやコンポーネントの階層構造を示します。
- **中央集権的なID管理**: すべてのIDを一箇所（例：__init__.py）に定義し、プロジェクト全体で一貫性のある管理を実現します。
- **エラー報告の向上**: エラーが発生した際に、どのページのどのコンポーネントのIDに問題があるかが明確になり、デバッグが容易になります。
- **エディタのサポート向上**: エディタのインデックス機能やオートコンプリート機能を活用し、開発速度を向上させ、タイプミスを減少させます。
- **宣言的なID定義**: データクラスを使用して宣言的にIDを管理し、ボイラープレートコードを削減し、コードの可読性を向上させます。
- **自動ケバブケース変換**: フィールド名を自動的にケバブケースに変換し、追加のコードなしで一貫したIDフォーマットを保証します。
- **不変で型安全**: フローズンデータクラスを利用してIDの整合性を保ち、ランタイムでの意図しない変更を防ぎます。

## インストール
pipを使用してインストールできます：

```bash
pip install dash-id-manager
```

## 使い方
以下は、Dash ID Managerを使用して効率的にIDを管理する高度な例です：

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

# すべてのIDグループを初期化
header_ids = DashboardHeaderIDs()
sidebar_ids = DashboardSidebarIDs()
content_ids = DashboardContentIDs()

# Dashコンポーネントでの使用例
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
````

## デモンストレーションされたメリット
- **階層的なグルーピング**: `DashboardIDs`は関連するすべてのコンポーネントIDをグループ化し、ページの構造を反映します。
- **自動プレフィックス**: 各サブクラス（`DashboardHeaderIDs`、`DashboardSidebarIDs`など）は自動的に親のプレフィックスを継承し、`dashboard-header-title` のようなIDを生成します。
- **中央集権的な管理**: すべてのIDが`__init__.py`に定義されており、容易にアクセス・修正が可能です。もちろん、他のファイルに分割しても構いません。
- **エラー報告の向上**: 構造化された命名により、ID関連のエラーが発生した際に影響を受けるページやコンポーネントが明確になります。
- **エディタサポート**: IDEが`dashboard_ids.header.title`などをオートコンプリートでき、タイプミスの可能性を減少させます。
- **宣言的な定義**: データクラスを使用して宣言的にIDを定義し、コードがよりクリーンで保守しやすくなります。
- **自動ケバブケース**: `logout_button` のようなフィールド名が自動的に `logout-button` に変換され、一貫性のあるIDフォーマットが保証されます。
- **不変のID**: フローズンデータクラスの使用により、IDがランタイムで変更されることなく整合性が保たれます。

## ライセンス
このプロジェクトはMITライセンスの下で提供されています。詳細は[LICENSEファイル](../LICENSE.md)を参照してください。