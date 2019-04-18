``` flow
st=>start: 开始
e=>end: 结束


login=>operation: 登录
loginsuccessful=>condition: 成功登陆?

st->login->loginsuccessful
loginsuccessful(no)->login


searchcondition=>operation: 设置检索条件
search=>operation: 查询
export=>condition: 数据导出?
download=>operation: 数据下载
searchfinished=>condition: 是否结束查询?

loginsuccessful(yes)->searchcondition->search->export
export(no)->searchfinished
export(yes)->download->searchfinished
searchfinished(no)->searchcondition


logout=>operation: 登出
searchfinished(yes)->logout->e
```

