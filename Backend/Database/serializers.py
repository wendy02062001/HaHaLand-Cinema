import rest_framework.serializers as serializers
import Database.models as models

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = ['maSP', 'tenSP', 'giaBan', 'hinhAnh', 'available', 'moTa', 'type']