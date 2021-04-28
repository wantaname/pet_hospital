import myconfig from "@/myconfig";

export default {
    // 页面标题
    header:"图片管理",
    // 搜索栏
    search:{
        // 下拉选择内容
        options:[
            {label:"文件名",value:"name"},
            {label:"备注",value:"note"},

        ],
        // 搜索列
        column:"name",
        keyword:"",
    },

    // 表格
    table:{
        table_columns:[
            {prop:"id",label:"ID",width:"180"},
            {prop:"name",label:"文件名",width:"180"},
            {prop:"path",label:"路径",width:"180"},
            {prop:"note",label:"备注",width:"180"},

        ],
    },


    //查看问题
    editInfo: {
        title: "问题",
        width: "55%",
        form: {
            id: {label: "id", name: "id", disabled: true, value: 1, type: "text"},
            case_name: {label: "病例名", name: "case_name", disabled: true, value: "", type: "text"},
            question: {label: "试题", name: "question", disabled: true, value: "", type: "textarea",rows:3},
            answer: {label: "答案", name: "answer", disabled: true, value: "", type: "textarea",rows:3},
            note:{label: "备注", name: "note", disabled: true, value: "", type: "textarea",rows:3},
            score:{label: "备注", name: "score", disabled: true, value: "", type: "text"},
        }
    },

    // 分页
    page: {
        pagenum: 1,
        pagesize: 10,
        total: 0
    },
    // upload_url:"http://127.0.0.1:5000/upload/uploadImage",
    upload_url:myconfig.baseURL+"/upload/uploadImage",
    // 请求
    request:{

        add:{
          url:"/upload/addImage",
          data:[]
        },
        delete:{
            url:"/upload/deleteImage",
            data:[],

        },
        getData:{
            url:"/upload/getImage",
            data:[]
        },
    }


}