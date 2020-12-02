<?php

/* Environment */
define( 'WP_ENVIRONMENT_TYPES', 'production' );

/* Database connection */
define( 'DB_NAME', 'wordpress' );
define( 'DB_USER', 'admin' );
define( 'DB_PASSWORD', 'User1234' );
define( 'DB_HOST', 'rds_ep' );
define( 'DB_CHARSET', 'utf8mb4' );
define( 'DB_COLLATE', 'utf8mb4_general_ci' );

/* Tables */
$table_prefix = 'wp29aii9_';

/* Security */
/* Security Keys */
define('AUTH_KEY',         '`w(QZ$O3[O<onOM6s!prU^]~0H7GQ22.^jyY60hK]*B%#_$e4j(WmjV/>I>F#Bq^');
define('SECURE_AUTH_KEY',  'V9~-y(KZy>6[U.w#/7];j{%B4)G^HHve5f;Z8gm}+H.wXl+:]-cA+r9EpH}R+%BO');
define('LOGGED_IN_KEY',    'd?O9Hu`ZB-a65k~su46EulPI,@.h`KV)S&?#:cWy2!,^%3|=x1K5s=z%30L/6&9,');
define('NONCE_KEY',        'iCgz=}SRFEOA$PU}SbG{gl$QxTI]xhZ4Z5-6|%z{I4#t&o|$Q+-3f<a&/0l:3QU>');
define('AUTH_SALT',        'B]<:3K_b89%$6?#f`t~+qC Vg#lDlGl^FV!&tg=3?-?SIBH+J<Bvj=Q-r&t( s1t');
define('SECURE_AUTH_SALT', ')T9${%t+,)U`9@WI<6OHqQN%fd%9[j{LrlP%ynx,% iG+bIbJPreIJ7JTVD:S]Yl');
define('LOGGED_IN_SALT',   'r{( 4*qN<e#o&k  ~,d_gE/wd>ZaI1!X-8]6r6c+?MEq5&mE6;;#`AGOnRaPr!gy');
define('NONCE_SALT',       'SG(=w)lQTOt qsw70lg-ffpW w2LPh%#hC0J_bb+>,,/vtva8lVVn&q-ZR9~s<?0');
/* HTTPS */
define( 'WP_DISABLE_FATAL_ERROR_HANDLER', false );
define( 'WP_DISABLE_ADMIN_EMAIL_VERIFY_SCREEN', false );

/* URL / Path */

/* Cookies */
define( 'TEST_COOKIE', 'wordpress_test_cookie' );
define( 'COOKIEHASH', 'nDAm44L9yF12GYz3w5vppPpWsnOtOpYOZ5HcxvLCm3xIQnE2CSa6WdybHIeJYegu' );
define( 'LOGGED_IN_COOKIE', 'wordpress_logged_in_nDAm44L9yF12GYz3w5vppPpWsnOtOpYOZ5HcxvLCm3xIQnE2CSa6WdybHIeJYegu' );
define( 'SECURE_AUTH_COOKIE', 'wordpress_logged_in_nDAm44L9yF12GYz3w5vppPpWsnOtOpYOZ5HcxvLCm3xIQnE2CSa6WdybHIeJYegu' );
define( 'AUTH_COOKIE', 'wordpress_nDAm44L9yF12GYz3w5vppPpWsnOtOpYOZ5HcxvLCm3xIQnE2CSa6WdybHIeJYegu' );
define( 'PASS_COOKIE', 'wordpresspass_nDAm44L9yF12GYz3w5vppPpWsnOtOpYOZ5HcxvLCm3xIQnE2CSa6WdybHIeJYegu' );
define( 'USER_COOKIE', 'wordpressuser_nDAm44L9yF12GYz3w5vppPpWsnOtOpYOZ5HcxvLCm3xIQnE2CSa6WdybHIeJYegu' );
define( 'RECOVERY_MODE_COOKIE', 'wordpress_rec_nDAm44L9yF12GYz3w5vppPpWsnOtOpYOZ5HcxvLCm3xIQnE2CSa6WdybHIeJYegu' );

/* Content */
define( 'AUTOSAVE_INTERVAL', 30 );
define( 'WP_POST_REVISIONS', 5 );
define( 'MEDIA_TRASH', true );
define( 'EMPTY_TRASH_DAYS', 7 );
define( 'WP_MAIL_INTERVAL', 86400 );

/* Memory */
define( 'WP_MEMORY_LIMIT', '128M' );
define( 'WP_MAX_MEMORY_LIMIT', '256M' );

/* Updating */
define( 'AUTOMATIC_UPDATER_DISABLED', false );
define( 'WP_AUTO_UPDATE_CORE', 'minor' );
define( 'CORE_UPGRADE_SKIP_NEW_BUNDLED', true );

/* File edition */
define( 'DISALLOW_FILE_MODS', false );
define( 'DISALLOW_FILE_EDIT', true );
define( 'IMAGE_EDIT_OVERWRITE', true );

/* Performance */
define( 'WP_CACHE', true );
define( 'WP_CACHE_KEY_SALT', 'g496n2qu8kcm482p2n:' );
define( 'COMPRESS_CSS', true );
define( 'COMPRESS_SCRIPTS', true );
define( 'CONCATENATE_SCRIPTS', false );
define( 'ENFORCE_GZIP', true );

/* Cron */
define( 'DISABLE_WP_CRON', false );
define( 'ALTERNATE_WP_CRON', false );
define( 'WP_CRON_LOCK_TIMEOUT', 60 );

/* FTP Access */

/* Plugins Must-Use */

/* Filtering */
define( 'DISALLOW_UNFILTERED_HTML', false );
define( 'ALLOW_UNFILTERED_UPLOADS', false );

/* Feed reader */
define( 'MAGPIE_CACHE_ON', true );
define( 'MAGPIE_CACHE_DIR', 'cache' );
define( 'MAGPIE_CACHE_AGE', 3600 );
define( 'MAGPIE_CACHE_FRESH_ONLY', false );
define( 'MAGPIE_DEBUG', false );
define( 'MAGPIE_USER_AGENT', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0' );
define( 'MAGPIE_FETCH_TIME_OUT', 5 );
define( 'MAGPIE_USE_GZIP', true );

/* MultiSite */
define( 'WP_ALLOW_MULTISITE', false );
define( 'WP_DEFAULT_THEME', 'twentytwenty' );

/* External URL Requests */
define( 'WP_HTTP_BLOCK_EXTERNAL', false );
if ( WP_HTTP_BLOCK_EXTERNAL ) {
	define( 'WP_ACCESSIBLE_HOSTS', '*.wordpress.org,*.github.com' );
}

/* File permissions */

/* Proxy */

/* Debug */
define( 'WP_DEBUG', false );
if ( WP_DEBUG ) {
	define( 'WP_DEBUG_DISPLAY', false );
	define( 'WP_DEBUG_LOG', false );
}
define( 'SCRIPT_DEBUG', false );
define( 'SAVEQUERIES', false );

/* Do not change anything else after this line! Thank you! */

if ( ! defined( 'ABSPATH' ) )
  define( 'ABSPATH', dirname( __FILE__ ) . '/' );
require_once ABSPATH . 'wp-settings.php';