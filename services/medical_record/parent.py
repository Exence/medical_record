from fastapi import (
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from database import get_session

from services.user import check_user_access_to_medcard

from models.child import Child
from models.parent import Parent, ParentUpdate, ParentCreate, ParentsResponse
from models.user import User

from tables import Parent, Child


class ParentService():
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, parent_id: int) -> Parent:
        parent = (
            self.session
            .query(Parent)
            .filter_by(id=parent_id)
            .first()
        )

        if not parent:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Parent is not found'
            )
        return parent
    
    def get_parents_by_medcard_num(self,  medcard_num: int):
        child = (self.session
                    .query(Child)
                    .filter_by(medcard_num=medcard_num)
                    .first()
                    )
        
        return ParentsResponse(father=child.father, mother=child.mother)
            

    def add_new_parent(self,  medcard_num: int, parent_data: ParentCreate):
        transaction = self.session.begin()
        try:
            parent = Parent(**{k: v for k,v in parent_data.dict().items() if k != 'parent_type'})
            self.session.add(parent)
            self.session.flush()  
            self.session.refresh(parent)

            child = (
                self.session
                .query(Child)
                .filter_by(medcard_num=medcard_num)
                .first()
            )
            setattr(child, f"{parent_data.parent_type.value}_id", parent.id)

            transaction.commit()
            transaction.close() 

            return parent
        except SQLAlchemyError as error:  
            print(error)
            transaction.rollback()
            transaction.close()
        
    def update_parent(self,  medcard_num: int, parent_data: ParentUpdate):
        parent = self._get(parent_data.id)
        for field, value in parent_data:
            setattr(parent, field, value)
        self.session.commit()
        return parent

    def delete_parent(self,  medcard_num: int, parent_id: int):
        parent = self._get(parent_id)
        self.session.delete(parent)
        self.session.commit()
        
    
