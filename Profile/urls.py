from django.conf.urls import url, patterns

urlpatterns = patterns("Profile.views",
                       url(r"^login$", "user_login", name="login"),
                       url(r"^logout$", "logout", name="logout"),
                       url(r"^register$", "register", name="register"),
                       url(r"^resetpwd$", "reset_password", name="reset_pwd"),
                       url(r"^mine/start$", "mine_start", name="mine_start"),
                       url(r"^mine/apply$", "mine_apply", name="mine_apply"),
                       url(r"^mine/group$", "mine_group", name="mine_group"),
                       url(r"^mine/like$", "mine_like", name="mine_like"),
                       url(r"^mine/info$", "mine_info", name="mine_info"),
                       url(r'^mine/exchange$', 'exchange_for_rmb', name='exchange'),
                       url(r"^mine/manage$", "manage_an_activity2", name="manage"),
                       url(r"^sendcode$", "send_verify_code", name="send_code"),
                       url(r"^user/modify$", "user_modify", name="user_modify"),
                       )