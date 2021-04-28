export default {
    // 页面标题
    header:"答题数据",
    // 搜索栏
    search:{
        // 下拉选择内容
        options:[
            {label: "用户名",value: "username"},
            {label: "考试",value: "exam_id"},
            {label:"题号",value:"question_id"},
            {label:"作答",value:"answer"},
            {label:"结果",value:"result"},
            {label:"得分",value:"score"}
        ],
        // 搜索列
        column:"username",
        keyword:"",
    },

    // 表格
    table:{
        table_columns:[
            {prop:"id",label:"ID",width:"180"},
            {prop:"username",label:"用户名",width:"180"},
            {prop:"exam_id",label:"考试",width:"180"},
            {prop:"question_id",label:"题号",width:"180"},
            {prop:"answer",label:"作答",width:"180"},
            {prop:"result",label:"结果",width:"180"},
            {prop:"score",label:"得分",width:"180"},
        ],
    },
    // 添加对话框
    addInfo: {
        title: "添加数据",
        width: "55%",
        form: {
            username: {label: "用户名", name: "username", disabled: false, value: "", type: "text"},
            exam_id: {label: "考试", name: "exam_id", disabled: false, value: "", type: "text"},
            question_id: {label: "题号", name: "question_id", disabled: false, value: "", type: "text"},
            answer: {label: "作答", name: "answer", disabled: false, value: "", type: "textarea",rows:3},
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
            score:{label: "分数", name: "score", disabled: true, value: "", type: "text"},
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
            url:"/exam_subject/add",
            data:["username",'question_id','answer','result',"score"]
        },
        delete:{
            url:"/exam_subject/delete",
            data:[],

        },
        getData:{
            url:"/exam_subject/getData",
            data:[]
        },
        edit:{
            url:"/exam_subject/edit",
            data:["id","username",'question_id','answer','result',"score"]
        }
    }


}