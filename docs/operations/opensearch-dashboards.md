# OpenSearch Dashboards 操作手册

OpenSearch Dashboards 是现有 OpenSearch `2.15.0` 的可选 Web 管理界面。它不替换 OpenSearch、不创建新的业务数据卷，也不修改现有 `l1_*_current` alias。

## 访问地址

使用服务器 Compose 配置时：

```text
服务器本机：http://127.0.0.1:5601
Tailscale：http://100.74.163.113:5601
```

当前 OpenSearch Security Plugin 已关闭，因此 Dashboards 没有登录页和用户权限。只能通过服务器本机或可信 Tailscale 网络访问，禁止绑定公网地址或 `0.0.0.0`。

## 首次启动

在服务器项目根目录执行：

```bash
git pull origin main

docker compose \
  -f compose.yaml \
  -f compose.server.yaml \
  --profile dashboards \
  up -d opensearch-dashboards
```

这条命令只新建或更新 `opensearch-dashboards`。依赖的 OpenSearch 已经运行时不会删除或重建其数据卷。

## 查看状态

```bash
docker compose \
  -f compose.yaml \
  -f compose.server.yaml \
  --profile dashboards \
  ps -a

curl -fsS http://127.0.0.1:5601/api/status \
  | jq '{state:.status.overall.state,title:.status.overall.title,version:.version.number}'
```

容器应为 `healthy`，API 状态应为 `green`，版本应为 `2.15.0`。

如果启动较慢：

```bash
docker compose \
  -f compose.yaml \
  -f compose.server.yaml \
  --profile dashboards \
  logs --tail=200 opensearch-dashboards
```

## 页面验证

浏览器打开：

```text
http://100.74.163.113:5601
```

进入左侧菜单的 `Dev Tools`，执行只读检查：

```http
GET _cat/aliases/l1_*?v
```

应看到以下 alias 指向 `*_v2`：

```text
l1_universities_current
l1_catalog_entries_current
l1_quick_facts_current
l1_sources_current
l1_entity_contexts_current
```

检查 MIT 目录数据：

```http
GET l1_catalog_entries_current/_search
{
  "size": 5,
  "query": {
    "bool": {
      "filter": [
        { "term": { "university_id": "mit" } },
        { "term": { "is_current": true } }
      ]
    }
  }
}
```

Dev Tools 具备写能力。不要执行 `DELETE`、`PUT mapping`、`update_by_query`、`reindex` 或 alias 修改操作。

## 重启

只重启 Dashboards：

```bash
docker compose \
  -f compose.yaml \
  -f compose.server.yaml \
  --profile dashboards \
  restart opensearch-dashboards
```

更新代码或配置后重新创建 Dashboards：

```bash
git pull origin main

docker compose \
  -f compose.yaml \
  -f compose.server.yaml \
  --profile dashboards \
  up -d --force-recreate opensearch-dashboards
```

更新整个服务栈并保持 Dashboards 启用：

```bash
docker compose \
  -f compose.yaml \
  -f compose.server.yaml \
  --profile dashboards \
  up -d --build
```

## 停止 Web 界面

```bash
docker compose \
  -f compose.yaml \
  -f compose.server.yaml \
  --profile dashboards \
  stop opensearch-dashboards
```

停止或删除 Dashboards 容器不会删除 OpenSearch 数据。禁止执行 `docker compose down -v`。
