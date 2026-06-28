# バックエンド基盤

## 目的

バックエンド実装を進める前段階として、CI、リンター、フォーマッター、型チェック、テスト実行の基盤を用意する。

この基盤は `fastapi/full-stack-fastapi-template` の方針を参考にしつつ、現時点ではフロントエンドに触れない。

## 採用ツール

- 依存関係管理と仮想環境管理: uv
- フォーマッター: Ruff format
- リンター: Ruff check
- 型チェック: mypy、ty
- テスト: pytest
- CI: GitHub Actions
- コミット前チェック: pre-commit

## ローカル実行

バックエンド依存関係を同期する。

```bash
cd backend
uv sync
```

バックエンドのチェックを実行する。

```bash
cd backend
uv run ruff format --check app tests
uv run ruff check app tests
uv run mypy app tests
uv run ty check app tests
uv run pytest
```

pre-commitを手動実行する。

```bash
pre-commit run --all-files
```

## CI

`.github/workflows/backend-ci.yml` は、`backend/`、`.python-version`、`.pre-commit-config.yaml`、ワークフロー自身が変更されたときに実行する。

現時点ではバックエンド基盤だけを対象にする。フロントエンド、Playwright、Docker Compose全体の検証は、対象ディレクトリや実装が追加された段階で別途追加する。
