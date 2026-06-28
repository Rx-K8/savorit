# データモデル

## 概要

データモデルは、個人向けのレシピ保存、検索、お気に入り、画像、調理履歴を支える。

認証はMVPに含まれるため、初期実装からユーザー所有権をモデル化する。

## エンティティ

### ユーザー（User）

アプリケーションのアカウントを表す。

主なフィールド:

- id
- email
- hashed_password
- display_name
- is_active
- is_superuser
- created_at
- updated_at

リレーション:

- レシピを所有する。
- お気に入りを所有する。
- 調理記録を所有する。

### レシピ（Recipe）

保存されたレシピを表す。

主なフィールド:

- id
- owner_id
- title
- description
- source_url
- memo
- servings
- created_at
- updated_at

リレーション:

- 1人のユーザーに属する。
- 材料を持つ。
- 手順を持つ。
- タグを持つ。
- レシピ画像を持つ。
- 調理記録を持つ。
- 所有者によってお気に入り登録できる。

### 材料（Ingredient）

レシピ内の1つの材料行を表す。

主なフィールド:

- id
- recipe_id
- name
- amount
- unit
- note
- position

### 手順（InstructionStep）

順序を持つ1つの調理手順を表す。

主なフィールド:

- id
- recipe_id
- body
- position

### タグ（Tag）

再利用可能なレシピラベルを表す。

主なフィールド:

- id
- owner_id
- name
- created_at

ルール:

- タグ名はユーザーごとに一意にする。
- 1つのレシピは複数のタグを持てる。
- 1つのタグは複数のレシピに紐づけられる。

### レシピ画像（RecipeImage）

レシピに添付された画像を表す。

主なフィールド:

- id
- recipe_id
- storage_key
- original_filename
- content_type
- file_size
- alt_text
- position
- created_at

ルール:

- MVPではファイルをローカルに保存する。
- データベースにはメタデータと `storage_key` を保存する。
- 画像バイナリ本体はPostgreSQLに保存しない。

### お気に入り（Favorite）

ユーザーがレシピをお気に入り登録したことを表す。

主なフィールド:

- id
- user_id
- recipe_id
- created_at

ルール:

- 1人のユーザーが同じレシピをお気に入り登録できるのは1回までとする。
- MVPでは、自分が所有するレシピのお気に入り登録だけを扱う。

### 調理記録（CookingLog）

ユーザーがレシピを作った記録を表す。

主なフィールド:

- id
- user_id
- recipe_id
- cooked_on
- memo
- created_at
- updated_at

リレーション:

- 1人のユーザーに属する。
- 1つのレシピに紐づけられる。
- 任意の調理記録画像を持つ。

### 調理記録画像（CookingLogImage）

調理記録に添付された画像を表す。

主なフィールド:

- id
- cooking_log_id
- storage_key
- original_filename
- content_type
- file_size
- alt_text
- position
- created_at

## 検索要件

MVPの検索は、以下を対象にしたキーワード検索をサポートする。

- レシピタイトル。
- レシピ説明。
- レシピメモ。
- 材料名。
- タグ名。

高度なランキング、表記ゆれ吸収、外部検索エンジンの導入はMVPに含めない。

## 所有権ルール

レシピ、タグ、お気に入り、画像、調理記録の操作は、すべて認証済みユーザーのスコープに限定する。

管理者ユーザーは運用目的で存在してよい。ただし、通常のレシピアクセスはデフォルトでユーザー単位に分離する。
