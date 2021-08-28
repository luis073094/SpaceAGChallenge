import graphene
from graphene_django import DjangoObjectType
from FieldWorker.models import FieldWorker


class FieldWorkerType(DjangoObjectType):
    class Meta:
        model = FieldWorker
        fields = ('id', 'first_name', 'last_name', 'function', 'created_at')

class Query(graphene.ObjectType):
    all_workers = graphene.List(FieldWorkerType)
    worker = graphene.Field(FieldWorkerType, worker_id=graphene.String())

    def resolve_all_workers(self, info, **kwargs):
        return FieldWorker.objects.all()

    def resolve_worker(self, info, worker_id):
        return FieldWorker.objects.get(pk=worker_id)


class createWorker(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        function = graphene.String(required=True)

    # Class attributes define the response of the mutation
    worker = graphene.Field(FieldWorkerType)

    @classmethod
    def mutate(cls, root, info, first_name, last_name, function):
        function = function.strip()

        if function.upper() != 'HARVEST' and function.upper() != 'PRUNNING' and function.upper() != 'SCOUTING' and function.upper() != 'OTHER':
            function = 'Other'

        newWorker = FieldWorker.objects.create(
            first_name = first_name,
            last_name = last_name,
            function = function
        )
        
        return createWorker(worker=newWorker)

class updateWorker(graphene.Mutation):
    class Arguments:
        id = graphene.String(required=True)
        first_name = graphene.String(required=False)
        last_name = graphene.String(required=False)
        function = graphene.String(required=False)

    # Class attributes define the response of the mutation
    worker = graphene.Field(FieldWorkerType)

    @classmethod
    def mutate(cls, root, info, id, first_name, last_name, function):
        updatedWorker = FieldWorker.objects.get(pk=id)

        function = function.strip()
        if function.upper() != 'HARVEST' and function.upper() != 'PRUNNING' and function.upper() != 'SCOUTING' and function.upper() != 'OTHER':
            function = 'Other'
        updatedWorker.function = function
        updatedWorker.first_name = first_name
        updatedWorker.last_name = last_name
        updatedWorker.save()

        return updateWorker(worker=updatedWorker)

class WorkerInput(graphene.InputObjectType):
    first_name = graphene.String()
    last_name = graphene.String()
    function = graphene.String()

class partialUpdateWorker(graphene.Mutation):
    class Arguments:
        id = graphene.String(required=True)
        input = WorkerInput(required=True)
        #first_name = graphene.String(required=False)
        #last_name = graphene.String(required=False)
        #function = graphene.String(required=False)

    # Class attributes define the response of the mutation
    worker = graphene.Field(FieldWorkerType)

    @classmethod
    def mutate(cls, root, info, id, input):
        updatedWorker = FieldWorker.objects.get(pk=id)

        if input.function is not None:
            function = input.function.strip()
            if function.upper() != 'HARVEST' and function.upper() != 'PRUNNING' and function.upper() != 'SCOUTING' and function.upper() != 'OTHER':
                function = 'Other'
            updatedWorker.function = function
        
        if input.first_name is not None:
            updatedWorker.first_name = input.first_name
        if input.last_name is not None:
            updatedWorker.last_name = input.last_name

        updatedWorker.save()

        return partialUpdateWorker(worker=updatedWorker)


class deleteWorker(graphene.Mutation):
    class Arguments:
        id = graphene.String(required=True)

    # Class attributes define the response of the mutation
    response = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, id):
        deleteWorkerObj = FieldWorker.objects.get(pk=id)
        deleteWorkerObj.delete()
        return deleteWorker(response=True)


class Mutation(graphene.ObjectType):
    create_worker = createWorker.Field()
    update_worker = updateWorker.Field()
    partial_update_worker = partialUpdateWorker.Field()
    delete_worker = deleteWorker.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
