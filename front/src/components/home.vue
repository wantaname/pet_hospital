<template>
  <el-container class="home-container"
                v-loading="loading"
                element-loading-spinner="el-icon-sunrise-1"
                element-loading-background="rgba(0, 0, 0, 0.88)">
    <!-- 頭部區域 -->
    <div id="particles">
      <vue-particles
        :color="particles.color"
        :particleOpacity="particles.particleOpacity"
        :particlesNumber="particles.particlesNumber"
        :shapeType="particles.shapeType"
        :particleSize="particles.particleSize"
        :linesColor="particles.linesColor"
        :linesWidth="particles.linesWidth"
        :lineLinked="particles.lineLinked"
        :lineOpacity="particles.lineOpacity"
        :linesDistance="particles.linesDistance"
        :moveSpeed="particles.moveSpeed"
        :hoverEffect="particles.hoverEffect"
        :hoverMode="particles.hoverMode"
        :clickEffect="particles.clickEffect"
        :clickMode="particles.clickMode"
        v-if="particlesShow"
      ></vue-particles>
    </div>
    <el-header>
      <div class="header">
        <!-- 圖標 -->
        <img class="logo" src="../assets/logo.png" alt />
        <span>虚拟宠物医院管理系统</span>
      </div>

      <div class="login" v-if="username==''">
        <el-button type="success" @click="login">登录</el-button>
<!--        <el-button type="success" @click="register">注册</el-button>-->
      </div>
      <div v-else>
        <el-avatar :src="avatar"></el-avatar>

        <el-dropdown @command="handleCommand">
  <span class="el-dropdown-link">
    <span style="color: #07F4DC">{{username}}</span><i class="el-icon-arrow-down el-icon--right"></i>
  </span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item command="exit">退出</el-dropdown-item>

          </el-dropdown-menu>
        </el-dropdown>
      </div>

    </el-header>

<!--    登录-->
    <el-dialog
        width="38%"
        title="登录"
        center
        :visible.sync="loginDialog"

        @close="loginClose">
<!--      表单-->
      <el-form :model="loginForm" :rules="loginRules" ref="ruleForm" label-width="88px" class="loginForm">
        <el-form-item label="用户名" prop="username">
          <el-input v-model="loginForm.username" placeholder="请输入用户名"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input placeholder="请输入密码" v-model="loginForm.password" show-password></el-input>
        </el-form-item>
      </el-form>

      <span slot="footer" class="dialog-footer">
    <el-button @click="loginDialog=false">取 消</el-button>
    <el-button type="primary" @click="loginConfirm">确 定</el-button>
  </span>
    </el-dialog>


    <!--    注册-->
    <el-dialog
        width="38%"
        title="注册"
        center
        :visible.sync="registerDialog"

        @close="registerClose">
      <!--      表单-->
      <el-form :model="registerForm" :rules="registerRules" ref="registerForm" label-width="88px" class="registerForm">
        <el-form-item label="用户名" prop="username">
          <el-input v-model="registerForm.username" placeholder="请输入用户名"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input placeholder="请输入密码" v-model="registerForm.password" show-password></el-input>
        </el-form-item>
      </el-form>

      <span slot="footer" class="dialog-footer">
    <el-button @click="registerClose">取 消</el-button>
    <el-button type="primary" @click="registerConfirm">确 定</el-button>
  </span>
    </el-dialog>

    <!-- 頁面主體區 -->
    <el-container>
      <!-- 側邊欄 -->
      <el-aside :width="isCollapse ? '64px' : '200px'">
        <el-menu
          :background-color="settingForm.menuBgColor"
          :text-color="settingForm.menuTextColor"
          :active-text-color="settingForm.menuActiveTextColor"
          :unique-opened="true"
          :collapse="isCollapse"
          :collapse-transition="false"
          :default-active="this.$route.path"
          router
        >
          <!-- 一級菜單 -->
          <el-submenu :index="item.id" v-for="item in menulist" :key="item.id">
            <!-- 一級菜單的模板區 -->
            <template slot="title">
              <!-- 圖標 -->
              <i :class="menuIcon[item.id]"></i>
              <!-- 文本 -->
              <span>{{item.name}}</span>
            </template>
            <!-- 二級菜單 -->
            <el-menu-item
              :index="'/'+subItem.path"
              v-for="subItem in item.children"
              :key="subItem.id"
            >
              <!-- 二級菜單模板 -->
              <template slot="title">
                <!-- 圖標 -->
                <i :class="submenuIcon[subItem.path]"></i>
                <!-- 文本 -->
                <span>{{subItem.name}}</span>

              </template>
            </el-menu-item>
          </el-submenu>
          <div class="footer">
            <!-- 设置 -->
            <div class="setting">
              <el-button
                type="info"
                icon="el-icon-setting"
                circle
                size="small"
                @click="drawer=true"
              ></el-button>
            </div>
            <!-- 折叠 -->
            <div class="toggle-button">
              <el-button
                type="info"
                icon="el-icon-s-fold"
                @click="toggleCollapse"
                size="small"
                circle
              ></el-button>
            </div>
          </div>
        </el-menu>
      </el-aside>
      <!-- 右側內容 -->
      <el-main :style="{ backgroundColor: settingForm.mainBgColor}">
        <!-- 路由佔位符 -->
        <router-view></router-view>
      </el-main>
    </el-container>

    <!-- 抽屉 -->
    <el-drawer :visible.sync="drawer" direction="rtl" :with-header="false">
      <el-form ref="settingForm" :model="settingForm" label-width="auto">
        <el-divider content-position="center">菜单栏</el-divider>
        <el-form-item label="背景颜色">
          <el-color-picker v-model="settingForm.menuBgColor"></el-color-picker>
        </el-form-item>
        <el-form-item label="文字颜色">
          <el-color-picker v-model="settingForm.menuTextColor"></el-color-picker>
        </el-form-item>
        <el-form-item label="激活颜色">
          <el-color-picker v-model="settingForm.menuActiveTextColor"></el-color-picker>
        </el-form-item>

        <el-divider content-position="center">内容区</el-divider>
        <el-form-item label="背景颜色">
          <el-color-picker v-model="settingForm.mainBgColor"></el-color-picker>
        </el-form-item>
        <el-divider content-position="center">二次元</el-divider>
        <el-form-item label="角色选择">
          <el-select v-model="live2dSetting.model" placeholder="请选择">
            <el-option
              v-for="item in modelOptions"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            ></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="方向">
          <el-select v-model="live2dSetting.direction" placeholder="请选择">
            <el-option
              v-for="item in directionOptions"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            ></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="水平偏移">
          <el-slider v-model="live2dSetting.hOffset" :min="-100" :max="800"></el-slider>
        </el-form-item>
        <el-form-item label="垂直偏移">
          <el-slider v-model="live2dSetting.vOffset" :min="-100" :max="800"></el-slider>
        </el-form-item>
        <el-form-item label="人物宽度">
          <el-slider v-model="live2dSetting.width" :min="80" :max="330"></el-slider>
        </el-form-item>
        <el-form-item label="人物高度">
          <el-slider v-model="live2dSetting.height" :min="160" :max="660"></el-slider>
        </el-form-item>

        <el-form-item label="开关">
          <el-switch
            v-model="live2dShow"
            active-color="#13ce66"
            inactive-color="#ff4949"
            :disabled="live2dShow"
          ></el-switch>
        </el-form-item>

        <el-divider content-position="center">特效</el-divider>
        <el-form-item label="开关">
          <el-switch
            v-model="particlesShow"
            active-color="#13ce66"
            inactive-color="#ff4949"
            :disabled="particlesShow"
          ></el-switch>
        </el-form-item>
        <el-form-item label="粒子颜色">
          <el-color-picker v-model="particles.color"></el-color-picker>
        </el-form-item>
        <el-form-item label=" 粒子透明度">
          <el-slider v-model="particles.particleOpacity" :min="0" :max="1" :step="0.1"></el-slider>
        </el-form-item>
        <el-form-item label="粒子数量">
          <el-slider v-model="particles.particlesNumber" :min="0" :max="800" :step="1"></el-slider>
        </el-form-item>
        <el-form-item label="粒子外观">
          <el-select v-model="particles.shapeType" placeholder="请选择">
            <el-option
              v-for="item in shapeTypeOptions"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            ></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="粒子大小">
          <el-slider v-model="particles.particleSize" :min="0" :max="100" :step="1"></el-slider>
        </el-form-item>

        <el-form-item label="线条颜色">
          <el-color-picker v-model="particles.linesColor"></el-color-picker>
        </el-form-item>

        <el-form-item label="线条宽度">
          <el-slider v-model="particles.linesWidth" :min="0" :max="20" :step="0.1"></el-slider>
        </el-form-item>

        <el-form-item label="是否连线">
          <el-switch v-model="particles.lineLinked" active-color="#13ce66" inactive-color="#ff4949"></el-switch>
        </el-form-item>
        <el-form-item label="线条透明度">
          <el-slider v-model="particles.lineOpacity" :min="0" :max="1" :step="0.1"></el-slider>
        </el-form-item>
        <el-form-item label="线条距离">
          <el-slider v-model="particles.linesDistance" :min="0" :max="500" :step="1"></el-slider>
        </el-form-item>

        <el-form-item label="粒子速度">
          <el-slider v-model="particles.moveSpeed" :min="0" :max="50" :step="0.5"></el-slider>
        </el-form-item>

        <el-form-item label="悬浮特效">
          <el-switch
            v-model="particles.hoverEffect"
            active-color="#13ce66"
            inactive-color="#ff4949"
          ></el-switch>
        </el-form-item>
        <el-form-item label="悬浮模式">
          <el-select v-model="particles.hoverMode" placeholder="请选择">
            <el-option
              v-for="item in hoverModeOptions"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            ></el-option>
          </el-select>
        </el-form-item>

        <el-form-item label="点击特效">
          <el-switch
            v-model="particles.clickEffect"
            active-color="#13ce66"
            inactive-color="#ff4949"
          ></el-switch>
        </el-form-item>

        <el-form-item label="点击模式">
          <el-select v-model="particles.clickMode" placeholder="请选择">
            <el-option
              v-for="item in clickModeOptions"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            ></el-option>
          </el-select>
        </el-form-item>
      </el-form>
    </el-drawer>

    <live2d :live2dSetting="live2dSetting" v-if="live2dShow"></live2d>
  </el-container>
</template>

<script>
import live2d from "./live2d";
import myconfig from "@/myconfig";
export default {
  data() {
    return {
      username:'',
      avatar:"",

      loginForm: {
        username:"",
        password:"",
      },
      loginRules:{
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
          { min: 3, max: 10, message: '长度在 3 到 10 个字符', trigger: 'blur' }
        ],
        password:[
          { required: true, message: '请输入密码', trigger: 'blur' },
          { min: 5, max: 15, message: '长度在 5 到 15 个字符', trigger: 'blur' }
        ],
      } ,
      //登录
      loginDialog:false,
      loading:false,
      //注册
      registerForm: {
        username:"",
        password:"",
      },
      registerRules:{
        username: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
          { min: 3, max: 10, message: '长度在 3 到 10 个字符', trigger: 'blur' }
        ],
        password:[
          { required: true, message: '请输入密码', trigger: 'blur' },
          { min: 5, max: 15, message: '长度在 5 到 15 个字符', trigger: 'blur' }
        ],
      } ,
      //登录
      registerDialog:false,
      // 抽屉
      drawer: false,
      // 菜单栏
      // 菜单栏设置表单
      settingForm: {
        menuBgColor: "",
        menuTextColor: "",
        menuActiveTextColor: "",
        mainBgColor: ""
      },
      // 二次元
      modelOptions: [
        { label: "chitose", value: "chitose" },
        { label: "epsilon2_1", value: "epsilon2_1" },
        { label: "gf", value: "gf" },
        { label: "haru_1", value: "haru_1" },
        { label: "haru_2", value: "haru_2" },
        { label: "haruto", value: "haruto" },

        { label: "hibiki", value: "hibiki" },
        { label: "hijiki", value: "hijiki" },
        { label: "izumi", value: "izumi" },
        { label: "koharu", value: "koharu" },
        { label: "miku", value: "miku" },
        { label: "nico", value: "nico" },

        { label: "nietzsche", value: "nietzsche" },
        { label: "ni-j", value: "ni-j" },
        { label: "nipsilon", value: "nipsilon" },
        { label: "nito", value: "nito" },
        { label: "shizuku", value: "shizuku" },
        { label: "tororo", value: "tororo" },
        { label: "tsumiki", value: "tsumiki" },
        { label: "unitychan", value: "unitychan" },
        { label: "wanko", value: "wanko" },
        { label: "z16", value: "z16" }
      ],
      directionOptions: [
        { label: "左下", value: "left" },
        { label: "右下", value: "right" },
        { label: "左上", value: "top" }
      ],

      // 看板娘
      live2dShow: false,
      live2dSetting: {
        model: "z16",
        width: 150,
        height: 300,
        direction: "right",
        hOffset: 0,
        vOffset: 0
      },
      // 特效
      particles: {
        color: "#dedede",
        particleOpacity: 0.7,
        particlesNumber: 80,
        shapeType: "circle",
        particleSize: 8,
        linesColor: "#dedede",
        linesWidth: 1,
        lineLinked: true,
        lineOpacity: 0.4,
        linesDistance: 150,
        moveSpeed: 3,
        hoverEffect: true,
        hoverMode: "grab",
        clickEffect: true,
        clickMode: "push"
      },
      particlesShow: false,
      shapeTypeOptions: [
        { label: "circle", value: "circle" },
        { label: "edge", value: "edge" },
        { label: "triangle", value: "triangle" },
        { label: "polygon", value: "polygon" },
        { label: "star", value: "star" }
      ],
      clickModeOptions: [
        { label: "推开", value: "push" },
        { label: "移除", value: "remove" },
        { label: "击退", value: "repulse" },
        { label: "气泡", value: "bubble" }
      ],
      hoverModeOptions: [
        { label: "聚集", value: "grab" },
        { label: "击退", value: "repulse" },
        { label: "气泡", value: "bubble" }
      ],

      // 菜单
      menulist: [
        //  项目介绍
        {
          "id":"0",
          "name":"医院导览",
          "children":[
            {"id":"0","name":"科室数据","path":"introduction"},
            // {"id":"1","name":"角色数据","path":"cosplay"}
          ]
        },
        //职能学习
        {
          "id":"1",
          "name":"职能学习",
          "children":[
            {"id":"0","name":"角色扮演","path":"cosplay"},
            // {"id":"1","name":"","path":"patientInfo"}
          ]
        },
        // 病例数据
        {
          "id":"2",
          "name":"病例数据",
          "children":[
            {
              "id": "0", "name": "病例表", "path": "case"
            },
            {
              "id":"1","name":"接诊表","path":"receive"
            }
            ,
            {
              "id":"2","name":"检查表","path":"inspect"
            },
            {
              "id":"3","name":"诊断结果表","path":"result"
            },
            {
              "id":"4","name":"治疗方案表","path":"cure"
            }
          ]
        },

        // 系统管理
        {
          "id":"3",
          "name":"系统管理",
          "children":[
            {
              "id":"0","name":"管理员","path":"administrator"
            },
            {
              "id":"1","name":"用户","path":"user"
            },

          ]
        },

        // 测试管理
        {
          "id":"4",
          "name":"测试管理",
          "children":[
            {
              "id":"0","name":"试题管理","path":"question"
            },
            {
              "id":"1","name":"考试数据","path":"user_exam"
            },
            {
              "id":"2","name":"答题数据","path":"exam_subject"
            }

          ]
        },

        // 统计分析
        {
          "id":"5",
          "name":"统计分析",
          "children":[
            {
              "id":"0","name":"分数统计","path":"score_analysis"
            },


          ]
        },
        // 统计分析

        // 统计分析
        // 常用功能
        {
          "id":"6",
          "name":"资源管理",
          "children":[
            {
              "id":"0","name":"图库","path":"image"
            },
            {
              id:"1",name:"视频库",path:"video"
            }
          ]
        },

      ],
      isCollapse: false,
      menuIcon: {
        "0": "el-icon-view",
        "1":"el-icon-s-custom",
        "2": "el-icon-data-analysis",
        "3": "el-icon-zoom-in",
        "4":"el-icon-notebook-1",
        "5":"el-icon-help",
        "6":"el-icon-loading",
        "7":"el-icon-s-promotion",
        "8":"el-icon-suitcase"
      },
      submenuIcon: {
        addPatient:"el-icon-edit",
        cosplay:"el-icon-s-flag",
        case:"el-icon-user-solid",
        question:"el-icon-notebook-1",
        receive:"el-icon-document-copy",
        introduction: "el-icon-document-copy",
        inspect:"el-icon-warning-outline",
        result:"el-icon-c-scale-to-original",
        cure:"el-icon-magic-stick",
        // question:"el-icon-circle-close",
        user_exam:"el-icon-aim",
        exam_subject:"el-icon-coin",
        score_analysis:"el-icon-data-analysis",
        image:"el-icon-picture-outline",
        video:"el-icon-video-camera",

        administrator:"el-icon-stopwatch",
        user:"el-icon-data-line",

        medicine:"el-icon-pie-chart",
        eatMedicine:"el-icon-paperclip",
        route:"el-icon-place",

        provinceIncrease:"el-icon-circle-plus",
        provinceCumulative:"el-icon-coin",
        cityIncrease:"el-icon-circle-plus-outline",
        cityCumulative:"el-icon-coin",

        operate:"el-icon-key",
        hospital:"el-icon-location-information",

        geography: "el-icon-location",
        books: "el-icon-notebook-2",
        class: "el-icon-menu",
        words: "el-icon-collection",
        degree: "el-icon-connection",
        cloud: "el-icon-cloudy",
        clothes: "el-icon-s-data",
        map: "el-icon-map-location",
        todo: "el-icon-notebook-2",

        age:"el-icon-thumb",
        sex:"el-icon-female",
        location:"el-icon-map-location",
      }
    };
  },
  created() {
    this.getUserName();
    this.avatar = myconfig.baseURL+"/static/image/default_avatar.png"

  },
  components: {
    live2d
  },
  methods: {
    //根据token获取用户名
    getUserName(){
      this.$http
          .get(`/administrator/getUserName`)
          .then(res => {
            if (res.status !== 200) return this.message.error("获取登录信息失败!");

            this.username = res.data.username
          })
          .catch(error => {
            console.log(error);
          });
    },
    handleCommand(command) {
      if(command=="exit") {
        this.exit()
      }
    },
    //退出
    exit(){
      this.username=""
      window.localStorage.setItem("token", "");
      return this.$message.info("退出成功！")
    },
    //登录
    login(){
      this.loginDialog=true
      this.loading=true
    },
    loginClose(){
      this.loading=false
    },

    loginConfirm(){
      this.$http
          .post("/administrator/login", {
            username:this.loginForm.username,
            password:this.loginForm.password
          })
          .then(res => {

            if (res.data.status == 404) {
              this.$message.error("用户未登录");

            }

            else if(res.data.status == 300)
            {

              return this.$message.error(res.data.msg)
            }
            else if (res.data.status == 200)
            {
              this.$message.success("登录成功！")
              window.localStorage.setItem("token", res.data.token);
              this.username=this.loginForm.username
              this.loginDialog=false
            }
          })
          .catch(error => {

            console.log(error);
            return this.$message.error("系统错误！");

          });
    },

    //注册
    register(){
      this.registerDialog=true
      this.loading=true
    },
    registerClose(){
      this.loading=false
    },
    registerConfirm(){
        this.$http
            .post("/administrator/register", {
              username:this.registerForm.username,
              password:this.registerForm.password
            })
            .then(res => {

              if (res.data.status == 404) {
                this.$message.error("用户未登录");

              }

              else if(res.data.status == 300)
              {

                return this.$message.error(res.data.msg)
              }
              else if (res.data.status == 200)
              {
                this.$message.success("注册成功！")
                this.registerDialog=false
              }
            })
            .catch(error => {

              console.log(error);
              return this.$message.error("系统错误！");

            });
      },
    // // 獲取菜單列表
    // async getMenuList() {
    //   const { data: res } = await this.$http.get(`menus`);
    //   if (res.status !== 200) return this.$message.error(res.msg);
    //   this.menulist = res.data;
    // },
    toggleCollapse() {
      this.isCollapse = !this.isCollapse;
    }
  }
};
</script>

<style lang="less" scoped>
#particles {
  width: 100%;
  height: 100%;
  position: fixed;
  z-index: -1;
  #particles-js {
    width: 100%;
    height: 100%;
  }
}
.el-container {
  height: 91%;

  .el-aside {
    height: 100%;
  }
}

.el-header {
  display: flex;

  justify-content: space-between;
  padding-left: 0;
  align-items: center;
  color: #ffffff;
  font-size: 20px;
  background-color: #0b0c0f;

  > div {
    display: flex;
    align-items: center;
    span {
      margin-left: 15px;
    }
  }
}
img.logo {
  height: 66px !important;
  border-radius: 50%;
}
.home-container {
  height: 100%;
}
.el-dropdown-link {
  cursor: pointer;
  color: #409EFF;
}
.el-icon-arrow-down {
  font-size: 12px;
}
.el-menu {
  border-right: none;
  width: 100%;
  height: 100%;
}

.header {
  margin-left: 10px;
}

.footer {
  position: absolute;
  width: 100%;
  bottom: 10px;
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;

  .el-button {
    margin: 0 10px;
  }
}

.el-form-item {
  margin-bottom: 10px;
}
.el-drawer {
  overflow: scroll;
  position: static !important;
}
.el-form {
  margin: 40px;
}
.loginForm{
  margin: 0;

  .el-form-item{
    margin-bottom: 25px;
  }

}

.registerForm{
  margin: 0;

  .el-form-item{
    margin-bottom: 25px;
  }

}
.wrap {
  height: 100%;
  width: 100%;
  position: relative;
}
</style>