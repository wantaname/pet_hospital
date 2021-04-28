export default {
    // 页面标题
    header:"角色扮演",

    // 搜索栏
    search:{
        // 下列选择内容
        options:[
            {label:"角色",value:"role"},
            {label:"工作",value:"work"},
            {label:"流程名",value:"process"},
            {label:"详细",value:"detail"},
            {label:"备注",value:"note"}
        ],

        // 搜索列
        column:"role",
        keyword:"",
    },

    table:{
        table_columns:[
            {prop:"id",label:"ID",width:"180"},
            {prop:"role",label:"角色",width:"180"},
            {prop:"work",label:"工作",width:"180"},
            {prop:"process",label:"流程名",width:"180"},
            {prop:"detail",label:"详细",width:"330"},
            {prop:"note",label:"备注",width:"180"},
        ],
    },
    // 添加对话框
    addInfo: {
        title: "添加数据",
        width: "55%",
        form: {
            role: {label: "角色", name: "role", disabled: false, value: "", type: "text"},
            work: {label: "工作", name: "work", disabled: false, value: "", type: "text"},
            process: {label: "流程名", name: "process", disabled: false, value: "", type: "text"},
            detail: {label: "详细", name: "detail", disabled: false, value: "", type: "textarea",rows:4},
            note: {label: "备注", name: "note", disabled: false, value: "", type: "text"},
        }
    },

    //编辑数据
    editInfo: {
        title: "编辑数据",
        width: "55%",
        form: {
            id: {label: "id", name: "id", disabled: true, value: 1, type: "text"},
            role: {label: "角色", name: "role", disabled: false, value: "", type: "text"},
            work: {label: "工作", name: "work", disabled: false, value: "", type: "text"},
            process: {label: "流程名", name: "process", disabled: false, value: "", type: "text"},
            detail: {label: "详细", name: "detail", disabled: false, value: "", type: "textarea",rows:4},
            note: {label: "备注", name: "note", disabled: false, value: "", type: "text"},
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
            url:"/cosplay/addProcess",
            data:["role",'work','process',"detail",'note']
        },
        delete:{
            url:"/cosplay/deleteProcess",
            data:[],

        },
        getData:{
            url:"/cosplay/getData",
            data:[]
        },
        edit:{
            url:"/cosplay/editProcess",
            data:["id","role",'work','process',"detail",'note']
        }
    }


}