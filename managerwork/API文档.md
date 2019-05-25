# API文档

#### 注册   post  /user 

​		上传user

​		返回ApiResponse



#### 登录   post  /user 

​		上传username password     

​		返回ApiResponse（token）



#### 修改用户信息 post  /user /{username}

​			上传 modifyRequest

​			返回ApiResponse

#### 创建问卷  post   /papers

​		上传paper 实例json

​		返回ApiResponse的 json 表示结果

​		



#### 发布问卷  post   /papers 只是状态变化了

​		上传 json {state：1}   // 1 

​		返回ApiResponse的 json 表示结果



#### 查询问卷  get search/{key_name}

​		返回的json对象 由以下三个属性

​		个数

​		返回 paper 实例的list

​		ApiResponse返回信息



#### 更新问卷   post /papers/{paper_id}

​		上传modifyRequest

​		返回ApiResponse的 json 表示结果



#### 删除问卷  post  /papers /{paper_id}
​               上传modifyRequest        
        
​		返回ApiResponse  json 



#### 获取用户全部的问卷  get  /user/{username}/paper

​		返回的json对象 由以下三个属性

​		返回个数

​		返回 paper 实例的list

​		ApiResponse

## 几个类的具体
```
User{
  id	integer($int64)  // 用户id
  nickname	string   //昵称
  studentid	string  //学号
  age	integer
  sex	string
  grade	string
  major	string
  image	string    // 头像
  email	string    
  password	string
  phone	string   
  User role   // 用户角色
}

Paper{
  id	integer($int64)
  creator	string   
  title	string   //问卷标题
  detail	string
  questions	array(Question)   // 问卷题目列表  是题目的list
  state	integer       //问卷状态  0 未发布/1 发布
  respondent	array(string)   //回答者  回答过问卷的user
  createdAt	Date
  closingDate	Date
  reward	integer    //奖励大小
}

Question{
    type	integer   //问题类型  1 单选  2 多选 3 问答
    content	string  // 问题描述
    items	array(string)   //选项列表  
    required	bool   // 是否必填
    anwser	array  (string)
    array of answer list
}
ApiResponse{
    code	integer($int32)
    state	bool  //表明是否成功了 0 成功 1 失败
    message	string  //表明成功或者失败的具体信息
}
//为了把put  delete 全改成post所设置的对象
modifyRequest {
    requestTpye： string 请求的类型  （有删除，更新等   update， delete）
    modifyClass： string  要修改的对象  （paper  user）
    userid：string
    data：{
        [title： tests ，detail：这是detail ] //修改的属性的json数组 , 如果是删除则没有
    } 
}


```

