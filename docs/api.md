# API

## 概要

APIは `/api/v1` 配下でバージョン管理する。

バックエンドが生成するOpenAPIスキーマを、フロントエンドおよび将来のモバイルクライアントの情報源とする。リクエスト・レスポンス型を手作業で維持するのではなく、このスキーマからTypeScriptクライアントを生成する。

## 認証

初期エンドポイント:

- `POST /api/v1/auth/register`
- `POST /api/v1/auth/login`
- `POST /api/v1/auth/logout`
- `POST /api/v1/auth/password-recovery`
- `POST /api/v1/auth/reset-password`
- `GET /api/v1/users/me`
- `PATCH /api/v1/users/me`

すべてのユーザーデータ用エンドポイントは認証で保護する。

認証方式はJWTベースを初期方針とする。ログアウトは、MVPではクライアント側のトークン破棄を基本とする。

## レシピ

初期エンドポイント:

- `GET /api/v1/recipes`
- `POST /api/v1/recipes`
- `GET /api/v1/recipes/{recipe_id}`
- `PATCH /api/v1/recipes/{recipe_id}`
- `DELETE /api/v1/recipes/{recipe_id}`

一覧の挙動:

- キーワード検索をサポートする。
- タグによる絞り込みをサポートする。
- お気に入り状態による絞り込みをサポートする。
- 認証済みユーザーが参照できるレシピだけを返す。

レシピ作成・更新では以下を扱う。

- タイトル。
- 説明。
- 参照元URL。
- メモ。
- 分量。
- 材料。
- 手順。
- タグ。

## レシピ画像

初期エンドポイント:

- `POST /api/v1/recipes/{recipe_id}/images`
- `DELETE /api/v1/recipes/{recipe_id}/images/{image_id}`

ルール:

- 画像はファイルとしてアップロードする。
- バックエンドは設定されたストレージバックエンド経由でファイルを保存する。
- MVPのストレージバックエンドはローカルファイルストレージとする。
- 画像メタデータはレシピレスポンスに含める。

## お気に入り

初期エンドポイント:

- `POST /api/v1/recipes/{recipe_id}/favorite`
- `DELETE /api/v1/recipes/{recipe_id}/favorite`

ルール:

- お気に入りは認証済みユーザーに属する。
- 同じお気に入り登録リクエストが繰り返されても、ユーザー視点では冪等に扱う。

## 調理記録

初期エンドポイント:

- `GET /api/v1/cooking-logs`
- `POST /api/v1/cooking-logs`
- `GET /api/v1/cooking-logs/{cooking_log_id}`
- `PATCH /api/v1/cooking-logs/{cooking_log_id}`
- `DELETE /api/v1/cooking-logs/{cooking_log_id}`

調理記録の作成・更新では以下を扱う。

- レシピ参照。
- 作った日。
- メモ。
- 任意の画像。

## 調理記録画像

初期エンドポイント:

- `POST /api/v1/cooking-logs/{cooking_log_id}/images`
- `DELETE /api/v1/cooking-logs/{cooking_log_id}/images/{image_id}`

## タグ

初期エンドポイント:

- `GET /api/v1/tags`
- `POST /api/v1/tags`
- `PATCH /api/v1/tags/{tag_id}`
- `DELETE /api/v1/tags/{tag_id}`

タグはユーザー単位に分離する。

## API設計ルール

- すべてのユーザーデータ用エンドポイントは認証を必須にする。
- すべてのユーザーデータ読み書きは認証済みユーザーのスコープに限定する。
- リクエスト・レスポンススキーマはOpenAPIに表現する。
- バックエンドバリデーションを正とする。
- クライアントに影響するAPI変更では、TypeScript APIクライアントを再生成する。
- MVP中に公開共有エンドポイントを追加しない。
