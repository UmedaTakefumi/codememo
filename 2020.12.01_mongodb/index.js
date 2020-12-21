const MongoClient = require('mongodb').MongoClient;
const assert = require('assert');

const url = 'mongodb://localhost:27017';
const db  = 'myMongo';

/* データベース接続 */
MongoClient.connect(url, (err, client) => {

  /* Errorがあれば処理を中断 */
  assert.equal(null, err);

  /* 接続に成功すればコンソールに表示 */
  console.log('Connected successfully to server');

  /** DBを取得 */
  const db = client.db(dbName);

  /* DBとの接続切断 */
  client.close();
});

// ref
// 	https://qiita.com/johnmackay150/items/df69fa05731ceb1af61c
