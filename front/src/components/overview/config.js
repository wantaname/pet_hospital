export default {
    // 页面标题
    header:"科室数据",

    // 搜索栏
    search:{
        // 下列选择内容
        options:[
            {label:"科室",value:"department"},
            {label:"负责人",value:"charge"}
        ],


        // 搜索列
        column:"department",
        keyword:"",
    },

    table:{
        table_columns:[
            {prop:"id",label:"ID",width:"180"},
            {prop:"department",label:"科室",width:"180"},
            {prop:"introduction",label:"功能",width:"330"},
            {prop:"charge",label:"负责人",width:"180"},
        ],
    },
    // 添加对话框
    addInfo: {
        title: "添加数据",
        width: "55%",
        form: {

            department: {label: "科室", name: "department", disabled: false, value: "", type: "text"},
            introduction: {label: "功能", name: "introduction", disabled: false, value: "", type: "textarea", rows: 4},
            charge: {label: "负责人", name: "charge", disabled: false, value: "", type: "text"}
        }
    },

    //编辑数据
    editInfo: {
        title: "编辑数据",
        width: "55%",
        form: {
            id: {label: "id", name: "id", disabled: true, value: 1, type: "text"},
            department: {label: "科室", name: "department", disabled: false, value: "", type: "text"},
            introduction: {label: "功能", name: "introduction", disabled: false, value: "", type: "textarea", rows: 4},
            charge: {label: "负责人", name: "charge", disabled: false, value: "", type: "text"}
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
            url:"/overview/addDepartment",
            data:["department",'introduction','charge']
        },
        delete:{
            url:"/overview/deleteDepartment",
            data:[],

        },
        getData:{
            url:"/overview/getData",
            data:[]
        },
        edit:{
            url:"/overview/editDepartment",
            data:["id","department",'introduction','charge']
        }
    }


}