# アーキテクチャ

## 概要

`savorit` はAPI優先の構成を採用する。ブラウザ向けフロントエンドと将来のモバイルクライアントは、同じバージョン付きHTTP APIを通じてバックエンドと通信する。

初期実装は `fastapi/full-stack-fastapi-template` の設計思想を参照する。具体的には、フロントエンドとバックエンドの分離、PostgreSQL、Dockerベースのローカル開発、OpenAPIから生成するフロントエンドAPIクライアント、自動テストを前提にする。

## バックエンド

バックエンドの標準スタックは以下とする。

- Python製HTTP API: FastAPI
- アプリケーションモデルとSQLデータベース操作: SQLModel
- データベースマイグレーション: Alembic
- 永続データベース: PostgreSQL
- Python依存関係と仮想環境管理: uv
- バックエンドテスト: Pytest
- コード品質: Ruffと型チェック

`uv` をバックエンドの標準パッケージ管理・環境管理ツールとする。Poetry、Pipenv、場当たり的な `pip install` ワークフローは導入しない。

バックエンドは以下を担当する。

- 認証と認可。
- ユーザーごとのレシピデータ。
- レシピ画像メタデータとファイルアクセス方針。
- 調理記録。
- OpenAPIスキーマ生成。

## フロントエンド

フロントエンドの標準スタックは以下とする。

- React.
- TypeScript.
- Vite.
- バックエンドのOpenAPIスキーマから生成するTypeScript APIクライアント。

フロントエンドは、バックエンドのバリデーション規則を真の情報源として重複管理してはならない。ユーザー体験向上のためのクライアント側バリデーションは許容するが、最終的な検証はバックエンドを正とする。

## API契約

OpenAPIスキーマを、バックエンドとクライアント間の契約とする。

ブラウザ向けフロントエンドは、手書きのリクエスト・レスポンス型ではなく、生成されたTypeScriptクライアントを通じてバックエンドを呼び出す。将来のExpo / React Nativeアプリも、同じAPI契約から互換クライアントを生成できるようにする。

## 認証

認証はMVPに含める。

初期認証スコープは以下とする。

- ユーザー登録。
- ログイン。
- ログアウト。
- パスワードリセット。
- 現在のユーザー情報取得。
- 管理者ユーザー。

認証方式はJWTベースを初期方針とする。MVPのログアウトはクライアント側のトークン破棄を基本とし、サーバー側のトークン失効リストやリフレッシュトークンの厳密なローテーションは、必要性が明確になった段階で追加検討する。

パスワードは平文で保存しない。パスワード保存はOWASPの指針に従い、現代的なパスワードハッシュ方式を使用する。

## 画像保存

MVPでは、アップロード画像をローカルファイルストレージに保存する。

実装では保存処理を境界の内側に閉じ込め、将来S3互換オブジェクトストレージへ移行する場合でも、レシピや調理記録のビジネスロジックを書き換えずに済むようにする。

データベースには画像メタデータと `storage_key` を保存する。ローカル保存の実装では、`storage_key` を保存先ファイルへの相対キーとして扱う。画像バイナリ本体はPostgreSQLに保存しない。

## データベースとマイグレーション

PostgreSQLを主データベースとする。

バックエンド実装開始後、スキーマ変更はAlembicマイグレーションとして管理する。マイグレーションを伴わない直接的なスキーマ変更はプロジェクトの標準ワークフローに含めない。

## モバイル展開方針

ネイティブモバイルアプリはMVPに含めない。

将来のモバイル開発では、別途方針変更がない限りExpo / React Nativeを候補とする。バックエンドAPIは、モバイルクライアントが認証、レシピ、画像、お気に入り、調理記録の各エンドポイントを再利用できるように設計する。

## 参考資料

- FastAPIフルスタックテンプレート: https://github.com/fastapi/full-stack-fastapi-template
- FastAPIのSQLデータベース解説: https://fastapi.tiangolo.com/tutorial/sql-databases/
- SQLModel: https://sqlmodel.tiangolo.com/
- uv公式ドキュメント: https://docs.astral.sh/uv/
- Vite公式ガイド: https://vite.dev/guide/
- OpenAPI Initiative公式情報: https://www.openapis.org/what-is-openapi
- OWASPパスワード保存チートシート: https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html
- FastAPIのOAuth2/JWT解説: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
- Expoプロジェクト作成ガイド: https://docs.expo.dev/get-started/create-a-project/
