<!DOCTYPE html>
<?php
    $dsn="mysql:host=localhost";
    $usuario="root";
    $clave="";
    try{
        $conexion=new PDO($dsn,$usuario,$clave);
        echo "SUCCESS";
        $create_database="CREATE DATABASE prueba1";
        $conexion->exec($create_database);
        echo "Database prueba1 creada";
    }
    catch (PDOException $execption){
        echo "fallo de conexion",$exception->getmessage();
    }
?>
</html>