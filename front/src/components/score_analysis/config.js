export default {
    // 页面标题
    header:"分数统计",
    // 搜索栏
    search:{
        // 下拉选择内容
        options:[
            {label: "用户名",value: "username"},
        ],
        // 搜索列
        column:"username",
        keyword:"",
    },

    // 表格
    table:{
        table_columns:[

            {prop:"username",label:"用户名",width:"180"},
            {prop:"score",label:"得分",width:"180"},

        ],
    },
    // 添加对话框
    addInfo: {
        title: "添加数据",
        width: "55%",
        form: {
            username: {label: "用户名", name: "username", disabled: false, value: "", type: "text"},
            question_id: {label: "题号", name: "question_id", disabled: false, value: "", type: "text"},
            answer: {label: "答案", name: "answer", disabled: false, value: "", type: "textarea",rows:3},
            result:{label: "结果", name: "result", disabled: false, value: "", type: "text"},
            score:{label: "得分", name: "score", disabled: false, value: "", type: "text"},
        }
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

    // 请求
    request:{
        add:{
            url:"/score_analysis/add",
            data:["username",'question_id','answer','result',"score"]
        },
        delete:{
            url:"/score_analysis/delete",
            data:[],

        },
        getData:{
            url:"/score_analysis/getData",
            data:[]
        },
        edit:{
            url:"/score_analysis/edit",
            data:["id","username",'question_id','answer','result',"score"]
        }
    }


}