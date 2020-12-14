import pytest
import mongomock
import  unittest
import json
import os
import time
import shutil, tempfile
from unittest import TestCase
from app.repository.tododb import TodoDB


class TestTodoDB:

    @classmethod
    def setup_class(cls):
        for k, v in sorted(os.environ.items()):
            print(k + ':', v)
        print('\n')

    @classmethod
    def teardown_class(cls):
        print("Teardown class: {} execution".format(cls.__name__))

    # def teardown_method(self):
    #     print(os.environ)
        # shutil.rmtree(cls.db_directory)

    @pytest.fixture()
    def some_data(self):
        data = {'foo': 1, 'bar': 2, 'baz': 3}
        return data

    @pytest.fixture
    def tododb(self):
        task1 = json.loads("""{
            "completed": false, 
            "created_on": "2020-11-26T09:33:20.627000", 
            "name": "first item", 
            "priority": "low"
          }""")

        task2 = json.loads("""{
            "completed": true, 
            "created_on": "2020-11-26T09:33:20.627000", 
            "name": "second item", 
            "priority": "medium"
          }""")

        task3 = json.loads("""{
            "completed": false, 
            "created_on": "2020-11-26T09:33:20.627000", 
            "name": "third item", 
            "priority": "high"
          }""")
        objects = [dict(task1), dict(task2), dict(task3)]
        return objects

    def test_foo(self, some_data):
        """Basic pytest fixture without unittest subclass
        https://github.com/nicoddemus/pytest-for-unittest-users/blob/master/PITCHME.md
        """
        assert some_data['foo'] == 1

    @pytest.mark.skip()
    def test_insert(self):
        self.fail()

    def test_get_all(self, tododb):
        collection = mongomock.MongoClient().db.collection
        print(tododb)
        collection.insert_many(tododb)
        print(list(collection.find()))
        result = list(collection.find())
        assert result[0]["name"] == "first item"
        assert result[0]["priority"] == "low"

        assert result[1]["name"] == "second item"
        assert result[1]["priority"] == "medium"

        assert result[2]["name"] == "third item"
        assert result[2]["priority"] == "high"


    @pytest.mark.skip()
    def test_get(self):
        self.fail()

    @pytest.mark.skip()
    def test_remove(self):
        self.fail()
