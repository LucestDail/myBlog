new Vue({
    delimiters: ['[[', ']]'],
    el: '#app',
    data: {
        title: 'Welcome to My Journal',
        days: [1,2,3]
    }
})

var app2 = new Vue({
  el: '#app-2',
  data: {
    message: '이 페이지는 ' + new Date() + ' 에 로드 되었습니다'
  }
})

var app3 = new Vue({
  el: '#app-3',
  data: {
    seen: true
  }
})