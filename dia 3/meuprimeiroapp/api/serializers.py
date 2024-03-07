from rest_framework.serializers import ModelSerializer

class PessoaSerializer(ModelSerializer):
    class Meta:
        model = PessoaBancoDeDados
        