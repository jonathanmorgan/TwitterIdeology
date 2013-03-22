from django.db import models

# depends on the tweetnet git project: https://github.com/jonathanmorgan/tweetnet.git
import tweetnet

class TweetIdeology( tweetnet.models.Abstract_Tweet ):

    # ideology variables.  Need to get these out, add them to an extended class
    #    or a separate class.
    outlet_label = models.CharField( max_length = 255, blank = True )
    outlet_id = models.IntegerField( null = True, blank = True )
    is_bbc = models.IntegerField( null = True, blank = True )
    is_cbs = models.IntegerField( null = True, blank = True )
    is_cnn = models.IntegerField( null = True, blank = True )
    is_drudge = models.IntegerField( null = True, blank = True )
    is_fox = models.IntegerField( null = True, blank = True )
    is_huffington = models.IntegerField( null = True, blank = True )
    is_msnbc = models.IntegerField( null = True, blank = True )
    is_nyt = models.IntegerField( null = True, blank = True )
    is_npr = models.IntegerField( null = True, blank = True )
    is_usatoday = models.IntegerField( null = True, blank = True )
    is_wsj = models.IntegerField( null = True, blank = True )
    is_wpo = models.IntegerField( null = True, blank = True )
    ideology = models.CharField( max_length = 255, blank = True )
    is_liberal = models.IntegerField( null = True, blank = True )
    is_conservative = models.IntegerField( null = True, blank = True )
    is_control = models.IntegerField( null = True, blank = True )
    ideology_int = models.IntegerField( null = True, blank = True )
    heterogeneity = models.CharField( max_length = 255, blank = True )
    is_low_h = models.IntegerField( null = True, blank = True )
    is_medium_h = models.IntegerField( null = True, blank = True )
    is_high_h = models.IntegerField( null = True, blank = True )
    heterogeneity_int = models.IntegerField( null = True, blank = True )


    #----------------------------------------------------------------------
    # instance methods
    #----------------------------------------------------------------------


#-- END class Tweet_Ideology --#


class Twitter_User_Ideology( tweetnet.models.Abstract_Twitter_User ):

    # aggregation fields.
    tweet_count = models.IntegerField( null = True, blank = True )
    tweet_retweet_count_mean = models.FloatField( null = True, blank = True )
    tweet_retweet_count_sum = models.IntegerField( null = True, blank = True )
    user_follower_count_max = models.IntegerField( null = True, blank = True )
    user_favorites_count_max = models.IntegerField( null = True, blank = True )
    tweet_user_mention_count_mean = models.FloatField( null = True, blank = True )
    tweet_user_mention_count_sum = models.IntegerField( null = True, blank = True )
    tweet_hashtag_mention_count_mean = models.FloatField( null = True, blank = True )
    tweet_hashtag_mention_count_sum = models.IntegerField( null = True, blank = True )
    tweet_url_count_mean = models.FloatField( null = True, blank = True )
    tweet_url_count_sum = models.IntegerField( null = True, blank = True )
    tweet_text_length_mean_1 = models.FloatField( null = True, blank = True )
    tweet_text_length_median = models.FloatField( null = True, blank = True )
    is_bbc_sum = models.IntegerField( null = True, blank = True )
    is_cbs_sum = models.IntegerField( null = True, blank = True )
    is_cnn_sum = models.IntegerField( null = True, blank = True )
    is_drudge_sum = models.IntegerField( null = True, blank = True )
    is_fox_sum = models.IntegerField( null = True, blank = True )
    is_huffington_sum = models.IntegerField( null = True, blank = True )
    is_msnbc_sum = models.IntegerField( null = True, blank = True )
    is_nyt_sum = models.IntegerField( null = True, blank = True )
    is_npr_sum = models.IntegerField( null = True, blank = True )
    is_usatoday_sum = models.IntegerField( null = True, blank = True )
    is_wsj_sum = models.IntegerField( null = True, blank = True )
    is_wpo_sum = models.IntegerField( null = True, blank = True )
    is_liberal_sum = models.IntegerField( null = True, blank = True )
    is_control_sum = models.IntegerField( null = True, blank = True )
    is_conservative_sum = models.IntegerField( null = True, blank = True )
    outlet_heterogeneity_low_sum = models.IntegerField( null = True, blank = True )
    outlet_heterogeneity_med_sum = models.IntegerField( null = True, blank = True )
    outlet_heterogeneity_high_sum = models.IntegerField( null = True, blank = True )
    is_bbc_max = models.IntegerField( null = True, blank = True )
    is_cbs_max = models.IntegerField( null = True, blank = True )
    is_cnn_max = models.IntegerField( null = True, blank = True )
    is_drudge_max = models.IntegerField( null = True, blank = True )
    is_fox_max = models.IntegerField( null = True, blank = True )
    is_huffington_max = models.IntegerField( null = True, blank = True )
    is_msnbc_max = models.IntegerField( null = True, blank = True )
    is_nyt_max = models.IntegerField( null = True, blank = True )
    is_npr_max = models.IntegerField( null = True, blank = True )
    is_usatoday_max = models.IntegerField( null = True, blank = True )
    is_wsj_max = models.IntegerField( null = True, blank = True )
    is_wpo_max = models.IntegerField( null = True, blank = True )
    diversity = models.FloatField( null = True, blank = True )
    ideology_count = models.IntegerField( null = True, blank = True )
    ideology_code = models.IntegerField( null = True, blank = True )


    #----------------------------------------------------------------------
    # instance methods
    #----------------------------------------------------------------------


#-- END class Twitter_User_Ideology --#