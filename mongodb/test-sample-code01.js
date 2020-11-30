// 管理ユーザ登録
// $ mongo --quiet localhost:27017/admin test-sample-code01.js 
//
// result:
//
//   Successfully added user: {
//   	"user" : "admin",
//   	"roles" : [
//   		{
//   			"role" : "root",
//   			"db" : "admin"
//   		}
//   	]
//   }

// ref:
// 	https://qiita.com/tomy0610/items/f540150ac8acaa47ff66
// 	https://qiita.com/yuiseki/items/1c656d6bab0307e1510c

db.createUser({user:"admin", pwd:"Zaq12wsx", roles:[{role:"root", db:"admin"}]})
