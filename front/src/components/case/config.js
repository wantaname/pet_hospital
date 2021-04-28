export default {
    // 页面标题
    header:"病例信息",

    // 搜索栏
    search:{
        // 下列选择内容
        options:[
            {label:"类型",value:"type"},
            {label:"病例名",value:"case_name"},
            {label:"文字",value:"text"},
            {label:"图片",value:"image"},
            {label:"视频",value:"video"},
        ],

        // 搜索列
        column:"case_name",
        keyword:"",
    },

    table:{
        table_columns:[
            {prop:"id",label:"ID",width:"180"},
            {prop:"type",label:"病例类型",width:"180"},
            {prop:"case_name",label:"病例名",width:"180"},
            {prop:"text",label:"文字",width:"180"},
            {prop:"image",label:"图片",width:"180"},
            {prop:"video",label:"视频",width:"180"},
        ],
    },
    // 添加对话框
    addInfo: {
        title: "添加数据",
        width: "55%",
        form: {
            type: {label: "病例类型", name: "type", disabled: false, value: "", type: "text"},
            case_name: {label: "病例名", name: "case_name", disabled: false, value: "", type: "text"},
            text: {label: "文字", name: "text", disabled: false, value: "", type: "text"},
            image: {label: "图片", name: "image", disabled: false, value: "", type: "text"},
            video:{label: "视频", name: "video", disabled: false, value: "", type: "text"},
        }
    },

    //编辑数据
    editInfo: {
        title: "编辑数据",
        width: "55%",
        form: {
            id: {label: "id", name: "id", disabled: true, value: 1, type: "text"},
            type: {label: "病例类型", name: "type", disabled: false, value: "", type: "text"},
            case_name: {label: "病例名", name: "case_name", disabled: false, value: "", type: "text"},
            text: {label: "文字", name: "text", disabled: false, value: "", type: "text"},
            image: {label: "图片", name: "image", disabled: false, value: "", type: "text"},
            video:{label: "视频", name: "video", disabled: false, value: "", type: "text"},
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
            url:"/case/addCase",
            data:["type","case_name",'text','image','video']
        },
        delete:{
            url:"/case/deleteCase",
            data:[],

        },
        getData:{
            url:"/case/getData",
            data:[]
        },
        edit:{
            url:"/case/editCase",
            data:["id","type","case_name",'text','image','video']
        }
    }


}