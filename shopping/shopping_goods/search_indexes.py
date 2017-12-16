from haystack import indexes
from shopping_goods.models import GoodsInfo


class GoodsInfoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, user_temlate=True)

    def get_model(self):
        return  GoodsInfo

    def index_queryset(self,using=None):
        return self.get_model().objects.all()