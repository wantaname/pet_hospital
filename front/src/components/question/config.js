export default {
    // 页面标题
    header:"试题管理",
    // 搜索栏
    search:{
        // 下拉选择内容
        options:[
            {label: "病种",value: "case_name"},
            {label:"试题",value:"question"},
            {label:"答案",value:"answer"},
            {label:"备注",value:"note"},
            {label:"分数",value:"score"}
        ],
        // 搜索列
        column:"case_name",
        keyword:"",
    },

    // 表格
    table:{
        table_columns:[
            {prop:"id",label:"ID",width:"180"},
            {prop:"case_name",label:"病种",width:"180"},
            {prop:"question",label:"试题",width:"180"},
            {prop:"answer",label:"答案",width:"180"},
            {prop:"note",label:"备注",width:"180"},
            {prop:"score",label:"分数",width:"180"},
        ],
    },
    // 添加对话框
    addInfo: {
        title: "添加数据",
        width: "55%",
        form: {
            case_name: {label: "病种", name: "case_name", disabled: false, value: "", type: "text"},
            question: {label: "试题", name: "question", disabled: false, value: "", type: "textarea",rows:3},
            answer: {label: "答案", name: "answer", disabled: false, value: "", type: "textarea",rows:3},
            note:{label: "备注", name: "note", disabled: false, value: "", type: "textarea",rows:3},
            score:{label: "分数", name: "score", disabled: false, value: "", type: "text"},
        }
    },

    //编辑对话框
    editInfo: {
        title: "编辑数据",
        width: "55%",
        form: {
            id: {label: "id", name: "id", disabled: true, value: 1, type: "text"},
            case_name: {label: "病种", name: "case_name", disabled: false, value: "", type: "text"},
            question: {label: "试题", name: "question", disabled: false, value: "", type: "textarea",rows:3},
            answer: {label: "答案", name: "answer", disabled: false, value: "", type: "textarea",rows:3},
            note:{label: "备注", name: "note", disabled: false, value: "", type: "textarea",rows:3},
            score:{label: "分数", name: "score", disabled: false, value: "", type: "text"},
        }
    },

    // 分页
    page: {
        pagenum: 1,
        pagesize: 10,
        total: 0
    },

    // 请求
    request:{
        add:{
            url:"/question/add",
            data:["case_name",'question','answer','note',"score"]
        },
        delete:{
            url:"/question/delete",
            data:[],

        },
        getData:{
            url:"/question/getData",
            data:[]
        },
        edit:{
            url:"/question/edit",
            data:["id","case_name",'question','answer','note',"score"]
        }
    }


}