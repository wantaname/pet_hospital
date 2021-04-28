export default {
    // 页面标题
    header:"管理员信息",

    // 搜索栏
    search:{
        // 下列选择内容
        options:[
            {label: "用户名",value: "username"},
            {label: "角色",value: "role"}
        ],

        // 搜索列
        column:"username",
        keyword:"",
    },

    table:{
        table_columns:[
            {prop:"id",label:"ID",width:"180"},
            {prop:"username",label:"用户名",width:"180"},
            {prop:"password",label:"密码",width:"180"},
            {prop:"role",label:"角色",width:"180"},
            {prop:"create_time",label:"创建时间",width:"180"},

        ],
    },
    // 添加对话框
    addInfo: {
        title: "添加数据",
        width: "55%",
        form: {
            username: {label: "用户名", name: "username", disabled: false, value: "", type: "text"},
            password: {label: "密码", name: "password", disabled: false, value: "", type: "text"},

        }
    },

    //编辑数据
    editInfo: {
        title: "编辑数据",
        width: "55%",
        form: {
            id: {label: "id", name: "id", disabled: true, value: 1, type: "text"},
            username: {label: "用户名", name: "username", disabled: false, value: "", type: "text"},
            password: {label: "密码", name: "password", disabled: false, value: "", type: "text"},
        }
    },

    // 分页
    page: {
        pagenum: 1,
        pagesize: 10,
        total: 0
    },


    // url
    request:{
        add:{
            url:"/administrator/add",
            data:["username",'password']
        },
        delete:{
            url:"/administrator/delete",
            data:[],

        },
        getData:{
            url:"/administrator/getData",
            data:[]
        },
        edit:{
            url:"/administrator/edit",
            data:["id","username",'password']
        }
    }


}