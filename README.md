# savorit

`savorit` は、レシピを載せて保管するためのアプリケーションです。

名前は、「味わう」「風味を楽しむ」という意味の **savor** と、「お気に入り」を意味する **favorite** を組み合わせたものです。お気に入りのレシピをひとつの場所に残し、また味わえるようにする、という意味を込めています。

## プロダクト方針

`savorit` は、個人が気に入ったレシピを登録し、検索し、後から見返し、実際に作った記録を残すためのアプリケーションです。

初期実装はブラウザで利用するアプリケーションとして進めます。ただし、将来的にスマートフォンアプリへ展開できるよう、FastAPIによるAPIを中心に置き、React + TypeScriptのフロントエンドとは分離して設計します。

## ドキュメント

今後の方針がぶれないよう、仕様と設計方針は以下のドキュメントで管理します。

- [プロダクト要求](docs/product-requirements.md)
- [アーキテクチャ](docs/architecture.md)
- [データモデル](docs/data-model.md)
- [API](docs/api.md)
- [開発フェーズ](docs/development-phases.md)
- [バックエンド基盤](docs/backend-tooling.md)

## 技術方針

- バックエンド: FastAPI + SQLModel + Alembic + PostgreSQL + uv
- フロントエンド: React + TypeScript + Vite
- API契約: OpenAPIスキーマと生成TypeScriptクライアント
- 認証: MVP初期からユーザー登録、ログイン、パスワードリセット、管理者ユーザーを扱う
- 画像: MVPではローカルファイル保存とし、将来S3互換オブジェクトストレージへ移行できる境界を用意する
- モバイル: MVPには含めないが、将来のExpo / React Nativeアプリが同じバックエンドを利用できるAPI優先設計にする
