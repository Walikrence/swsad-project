# API文档

#### 注册   post  /user 

​		上传user

​		返回ApiResponse



#### 登录   post  /user 

​		上传username password

​		返回ApiResponse（token）



#### 修改信息 put  /user /{username}

​			上传修改的属性的json数组 如    {major： 软件工程，age： 20 }

​			返回ApiResponse

#### 创建问卷  post   /papers

​		上传paper 实例json

​		返回ApiResponse的 json 表示结果

​		



#### 发布问卷  post   /papers 只是状态变化了

​		上传 json {state：1}

​		返回ApiResponse的 json 表示结果



#### 查询问卷  get search/{key_name}

​		返回的json对象 由以下三个属性

​		个数

​		返回 paper 实例的list

​		ApiResponse返回信息



#### 更新问卷   put /papers/{paper_id}

​		上传修改的属性的json数组 如 {title： tests ，detail：这是detail }

​		返回ApiResponse的 json 表示结果



#### 删除问卷  delete  /papers /{paper_id}

​		返回ApiResponse  json 



#### 获取用户全部的问卷  get  /user/{username}/paper

​		返回的json对象 由以下三个属性

​		返回个数

​		返回 paper 实例的list

​		ApiResponse

## 几个类的具体
```
User{
  id	integer($int64)
  nickname	string
  studentid	string
  age	integer
  sex	string
  grade	string
  major	string
  image	string
  email	string
  password	string
  phone	string
  userStatus	integer($int32)
  User role
}

Paper{
  id	integer($int64)
  creator	string
  title	string
  detail	string
  questions	array(Question)
  state	integer
  respondent	array(string)
  createdAt	Date
  default: new Date()
  closingDate	Date
  default: new Date()
  reward	integer
}

Question{
    type	integer
    content	string
    items	array(string)
    required	bool
    whether it is must
    anwser	array(string)
    array of answer list
}
ApiResponse{
    code	integer($int32)
    state	bool
    表明是否成功了 0 成功 1 失败

    message	string
    表明成功或者失败的具体信息

}


```

