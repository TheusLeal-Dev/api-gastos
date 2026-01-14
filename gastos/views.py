from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from .models import Gasto
from .serializers import GastoSerializer

class GastoViewSet(viewsets.ModelViewSet):
    queryset = Gasto.objects.all().order_by("-created_at")
    serializer_class = GastoSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        categoria = self.request.query_params.get("categoria")
        concluido = self.request.query_params.get("concluido")  # "true" / "false"

        if categoria:
            qs = qs.filter(categoria__iexact=categoria)

        if concluido is not None:
            if concluido.lower() in ["true", "1", "yes"]:
                qs = qs.filter(concluido=True)
            elif concluido.lower() in ["false", "0", "no"]:
                qs = qs.filter(concluido=False)

        return qs

    @action(detail=False, methods=["get"], url_path="total")
    def total(self, request):
        qs = self.get_queryset()

        total_pendente = qs.filter(concluido=False).aggregate(s=Sum("valor"))["s"] or 0
        total_concluido = qs.filter(concluido=True).aggregate(s=Sum("valor"))["s"] or 0
        total_geral = qs.aggregate(s=Sum("valor"))["s"] or 0

        return Response({
            "pendente": float(total_pendente),
            "concluido": float(total_concluido),
            "geral": float(total_geral),
        })

    @action(detail=False, methods=["get"], url_path="categorias")
    def categorias(self, request):
        cats = (
            Gasto.objects.values_list("categoria", flat=True)
            .distinct()
            .order_by("categoria")
        )
        # tira vazios e normaliza
        cats = [c for c in cats if c and str(c).strip()]
        return Response({"categorias": cats})
